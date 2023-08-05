# SPDX-License-Identifier: MIT
# Copyright (c) 2022 MBition GmbH
from collections import OrderedDict
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, List, Optional

from .dataobjectproperty import DataObjectProperty, DopBase
from .decodestate import DecodeState
from .encodestate import EncodeState
from .exceptions import DecodeError, EncodeError
from .globals import logger
from .odxlink import OdxDocFragment, OdxLinkDatabase, OdxLinkId, OdxLinkRef
from .odxtypes import odxstr_to_bool
from .specialdata import create_sdgs_from_et
from .structures import BasicStructure
from .utils import create_description_from_et

if TYPE_CHECKING:
    from .diaglayer import DiagLayer


@dataclass
class MultiplexerCase:
    """This class represents a Case which represents multiple options in a Multiplexer."""

    short_name: str
    long_name: str
    structure_ref: OdxLinkRef
    lower_limit: str
    upper_limit: str

    def __post_init__(self) -> None:
        self._structure: Optional[BasicStructure] = None

    @staticmethod
    def from_et(et_element, doc_frags: List[OdxDocFragment]) -> "MultiplexerCase":
        """Reads a Case for a Multiplexer."""
        short_name = et_element.findtext("SHORT-NAME")
        long_name = et_element.findtext("LONG-NAME")
        structure_ref = OdxLinkRef.from_et(et_element.find("STRUCTURE-REF"), doc_frags)
        assert structure_ref is not None
        lower_limit = et_element.findtext("LOWER-LIMIT")
        upper_limit = et_element.findtext("UPPER-LIMIT")

        return MultiplexerCase(
            short_name=short_name,
            long_name=long_name,
            structure_ref=structure_ref,
            lower_limit=lower_limit,
            upper_limit=upper_limit,
        )

    def _build_odxlinks(self) -> Dict[OdxLinkId, Any]:
        return {}

    def _resolve_odxlinks(self, odxlinks: OdxLinkDatabase) -> None:
        self._structure = odxlinks.resolve(self.structure_ref)

    def _resolve_snrefs(self, diag_layer: "DiagLayer") -> None:
        pass

    def __repr__(self) -> str:
        return (f"MultiplexerCase('{self.short_name}', " + ", ".join([
            f"lower_limit='{self.lower_limit}'",
            f"upper_limit='{self.upper_limit}'",
            f"structure_ref='{self.structure_ref}'",
        ]) + ")")


@dataclass
class MultiplexerDefaultCase:
    """This class represents a Default Case, which is selected when there are no cases defined in the Multiplexer."""

    short_name: str
    long_name: str
    structure_ref: Optional[OdxLinkRef]

    def __post_init__(self) -> None:
        self._structure: Optional[BasicStructure] = None

    @staticmethod
    def from_et(et_element, doc_frags: List[OdxDocFragment]) -> "MultiplexerDefaultCase":
        """Reads a Default Case for a Multiplexer."""
        short_name = et_element.findtext("SHORT-NAME")
        long_name = et_element.findtext("LONG-NAME")

        structure_ref = OdxLinkRef.from_et(et_element.find("STRUCTURE-REF"), doc_frags)

        return MultiplexerDefaultCase(
            short_name=short_name,
            long_name=long_name,
            structure_ref=structure_ref,
        )

    def _build_odxlinks(self) -> Dict[OdxLinkId, Any]:
        return {}

    def _resolve_odxlinks(self, odxlinks: OdxLinkDatabase) -> None:
        if self.structure_ref is not None:
            self._structure = odxlinks.resolve(self.structure_ref)

    def _resolve_snrefs(self, diag_layer: "DiagLayer") -> None:
        pass

    def __repr__(self) -> str:
        return (f"MultiplexerDefaultCase('{self.short_name}', " + ", ".join([
            f"structure_ref='{self.structure_ref}'",
        ]) + ")")


@dataclass
class MultiplexerSwitchKey:
    """This class represents a Switch Key, which is used to select one of the cases defined in the Multiplexer."""

    byte_position: int
    bit_position: Optional[int]
    dop_ref: OdxLinkRef

    def __post_init__(self):
        self._dop: DataObjectProperty = None  # type: ignore

    @staticmethod
    def from_et(et_element, doc_frags: List[OdxDocFragment]) -> "MultiplexerSwitchKey":
        """Reads a Switch Key for a Multiplexer."""
        byte_position = int(et_element.findtext("BYTE-POSITION", "0"))
        assert byte_position is not None
        bit_position_str = et_element.findtext("BIT-POSITION")
        bit_position = int(bit_position_str) if bit_position_str is not None else None
        dop_ref = OdxLinkRef.from_et(et_element.find("DATA-OBJECT-PROP-REF"), doc_frags)
        assert dop_ref is not None

        return MultiplexerSwitchKey(
            byte_position=byte_position,
            bit_position=bit_position,
            dop_ref=dop_ref,
        )

    def _build_odxlinks(self) -> Dict[OdxLinkId, Any]:
        return {}

    def _resolve_odxlinks(self, odxlinks: OdxLinkDatabase) -> None:
        dop = odxlinks.resolve(self.dop_ref)
        if isinstance(dop, DataObjectProperty):
            self._dop = dop
        else:
            logger.warning(
                f"DATA-OBJECT-PROP-REF '{self.dop_ref}' could not be resolved in SWITCH-KEY.")

    def _resolve_snrefs(self, diag_layer: "DiagLayer") -> None:
        pass

    def __repr__(self) -> str:
        return (f"MultiplexerSwitchKey(" + ", ".join([
            f"byte_position={self.byte_position}",
            f"bit_position={self.bit_position}",
            f"dop_ref={self.dop_ref}",
        ]) + ")")


@dataclass
class Multiplexer(DopBase):
    """This class represents a Multiplexer (MUX) which are used to interpret data stream depending on the value
    of a switch-key (similar to switch-case statements in programming languages like C or Java)."""

    byte_position: int
    switch_key: MultiplexerSwitchKey
    default_case: Optional[MultiplexerDefaultCase]
    cases: List[MultiplexerCase]

    @staticmethod
    def from_et(et_element, doc_frags: List[OdxDocFragment]) -> "Multiplexer":
        """Reads a Multiplexer from Diag Layer."""
        odx_id = OdxLinkId.from_et(et_element, doc_frags)
        assert odx_id is not None
        short_name = et_element.findtext("SHORT-NAME")
        long_name = et_element.findtext("LONG-NAME")
        description = create_description_from_et(et_element.find("DESC"))
        is_visible_raw = odxstr_to_bool(et_element.get("IS-VISIBLE"))
        sdgs = create_sdgs_from_et(et_element.find("SDGS"), doc_frags)
        byte_position = int(et_element.findtext("BYTE-POSITION", "0"))
        switch_key = MultiplexerSwitchKey.from_et(et_element.find("SWITCH-KEY"), doc_frags)

        default_case = None
        if et_element.find("DEFAULT-CASE") is not None:
            default_case = MultiplexerDefaultCase.from_et(
                et_element.find("DEFAULT-CASE"), doc_frags)

        cases = []
        if et_element.find("CASES") is not None:
            cases = [
                MultiplexerCase.from_et(el, doc_frags)
                for el in et_element.find("CASES").iterfind("CASE")
            ]

        logger.debug("Parsing MUX " + short_name)

        return Multiplexer(
            odx_id=odx_id,
            short_name=short_name,
            long_name=long_name,
            description=description,
            sdgs=sdgs,
            is_visible_raw=is_visible_raw,
            byte_position=byte_position,
            switch_key=switch_key,
            default_case=default_case,
            cases=cases,
        )

    @property
    def bit_length(self):
        return None

    def _get_case_limits(self, case: MultiplexerCase):
        key_type = self.switch_key._dop.physical_type.base_data_type
        lower_limit = key_type.make_from(case.lower_limit)
        upper_limit = key_type.make_from(case.upper_limit)
        return lower_limit, upper_limit

    def convert_physical_to_bytes(self, physical_value, encode_state: EncodeState,
                                  bit_position: int) -> bytes:

        if bit_position != 0:
            raise EncodeError("Multiplexer must be aligned, i.e. bit_position=0, but "
                              f"{self.short_name} was passed the bit position {bit_position}")

        if not isinstance(physical_value, dict) or len(physical_value) != 1:
            raise EncodeError("""Multiplexer should be defined as a dict
            with only one key equal to the desired case""")

        case_name, case_value = next(iter(physical_value.items()))
        key_pos = self.switch_key.byte_position
        case_pos = self.byte_position

        for case in self.cases or []:
            if case.short_name == case_name:
                if case._structure:
                    case_bytes = case._structure.convert_physical_to_bytes(
                        case_value, encode_state, 0)
                else:
                    case_bytes = bytes()

                key_value, _ = self._get_case_limits(case)
                sk_bit_position = self.switch_key.bit_position
                sk_bit_position = sk_bit_position if sk_bit_position is not None else 0
                key_bytes = self.switch_key._dop.convert_physical_to_bytes(
                    key_value, encode_state, sk_bit_position)

                mux_len = max(len(key_bytes) + key_pos, len(case_bytes) + case_pos)
                mux_bytes = bytearray(mux_len)
                mux_bytes[key_pos:key_pos + len(key_bytes)] = key_bytes
                mux_bytes[case_pos:case_pos + len(case_bytes)] = case_bytes

                return bytes(mux_bytes)

        raise EncodeError(f"The case {case_name} is not found in Multiplexer {self.short_name}")

    def convert_bytes_to_physical(self, decode_state: DecodeState, bit_position: int = 0):

        if bit_position != 0:
            raise DecodeError("Multiplexer must be aligned, i.e. bit_position=0, but "
                              f"{self.short_name} was passed the bit position {bit_position}")
        byte_code = decode_state.coded_message[decode_state.next_byte_position:]
        key_decode_state = DecodeState(
            coded_message=byte_code[self.switch_key.byte_position:],
            parameter_values=dict(),
            next_byte_position=0,
        )
        bit_position_int = (
            self.switch_key.bit_position if self.switch_key.bit_position is not None else 0)
        key_value, key_next_byte = self.switch_key._dop.convert_bytes_to_physical(
            key_decode_state, bit_position=bit_position_int)

        case_decode_state = DecodeState(
            coded_message=byte_code[self.byte_position:],
            parameter_values=dict(),
            next_byte_position=0,
        )
        case_found = False
        case_next_byte = 0
        case_value = None
        for case in self.cases or []:
            lower, upper = self._get_case_limits(case)
            if lower <= key_value and key_value <= upper:
                case_found = True
                if case._structure:
                    case_value, case_next_byte = case._structure.convert_bytes_to_physical(
                        case_decode_state)
                break

        if not case_found and self.default_case is not None:
            case_found = True
            if self.default_case._structure:
                case_value, case_next_byte = self.default_case._structure.convert_bytes_to_physical(
                    case_decode_state)

        if not case_found:
            raise DecodeError(
                f"Failed to find a matching case in {self.short_name} for value {key_value}")

        mux_value = OrderedDict({case.short_name: case_value})
        mux_next_byte = decode_state.next_byte_position + max(
            key_next_byte + self.switch_key.byte_position, case_next_byte + self.byte_position)
        return mux_value, mux_next_byte

    def _build_odxlinks(self) -> Dict[OdxLinkId, Any]:
        odxlinks = super()._build_odxlinks()

        return odxlinks

    def _resolve_odxlinks(self, odxlinks: OdxLinkDatabase) -> None:
        super()._resolve_odxlinks(odxlinks)

        self.switch_key._resolve_odxlinks(odxlinks)
        if self.default_case is not None:
            self.default_case._resolve_odxlinks(odxlinks)

        for case in self.cases:
            case._resolve_odxlinks(odxlinks)

    def _resolve_snrefs(self, diag_layer: "DiagLayer"):
        super()._resolve_snrefs(diag_layer)

        self.switch_key._resolve_snrefs(diag_layer)
        if self.default_case is not None:
            self.default_case._resolve_snrefs(diag_layer)

        for case in self.cases:
            case._resolve_snrefs(diag_layer)

    def __repr__(self) -> str:
        return (f"Multiplexer('{self.short_name}', " + ", ".join([
            f"odx_id='{self.odx_id}'",
            f"byte_position='{self.byte_position}'",
            f"switch_key='{self.switch_key}'",
            f"default_case='{self.default_case}'",
            f"cases='{self.cases}'",
        ]) + ")")
