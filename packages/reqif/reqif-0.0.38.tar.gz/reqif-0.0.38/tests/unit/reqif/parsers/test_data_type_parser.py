from lxml import etree

from reqif.models.reqif_data_type import (
    ReqIFDataTypeDefinitionEnumeration,
    ReqIFDataTypeDefinitionString,
)
from reqif.parsers.data_type_parser import (
    DataTypeParser,
)


def test_01_string_type() -> None:
    spec_type_string = """
    <DATATYPE-DEFINITION-STRING
        IDENTIFIER="TEST_DATATYPE_IDENTIFIER"
        LAST-CHANGE="2021-10-14T10:11:59.495+02:00"
        LONG-NAME="T_String32k"
        MAX-LENGTH="32000"/>
    """
    spec_type_xml = etree.fromstring(spec_type_string)
    data_type = DataTypeParser.parse(spec_type_xml)
    assert isinstance(data_type, ReqIFDataTypeDefinitionString)

    assert data_type.identifier == "TEST_DATATYPE_IDENTIFIER"


def test_02_enumeration_type():
    spec_type_string = """
<DATATYPE-DEFINITION-ENUMERATION
  IDENTIFIER="NODE_TYPE"
  LAST-CHANGE="2015-12-14T02:04:51.764+01:00"
  LONG-NAME="T_Kind">
  <SPECIFIED-VALUES>
    <ENUM-VALUE
      IDENTIFIER="NODE_TYPE_SECTION"
      LAST-CHANGE="2015-12-14T02:04:51.764+01:00"
      LONG-NAME="ordinary"
    >
      <PROPERTIES>
        <EMBEDDED-VALUE KEY="1"/>
      </PROPERTIES>
    </ENUM-VALUE>
    <ENUM-VALUE
      IDENTIFIER="NODE_TYPE_REQUIREMENT"
      LAST-CHANGE="2015-12-14T02:04:51.765+01:00"
      LONG-NAME="Table"
    >
      <PROPERTIES>
        <EMBEDDED-VALUE KEY="2"/>
      </PROPERTIES>
    </ENUM-VALUE>
  </SPECIFIED-VALUES>
</DATATYPE-DEFINITION-ENUMERATION>
    """
    spec_type_xml = etree.fromstring(spec_type_string)

    data_type = DataTypeParser.parse(spec_type_xml)
    assert isinstance(data_type, ReqIFDataTypeDefinitionEnumeration)

    assert data_type.identifier == "NODE_TYPE"
    assert len(data_type.values_map) == 2

    value_1 = data_type.values_map["NODE_TYPE_SECTION"]
    value_2 = data_type.values_map["NODE_TYPE_REQUIREMENT"]

    assert value_1.key == "1"
    assert value_2.key == "2"
