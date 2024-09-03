import allure
import pytest

def test_conformance_0():
    allure.dynamic.title("00 The key words MAY, MUST, MUST NOT, OPTIONAL, RECOMMENDED, REQUIRED, and SHOULD in this document are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all capitals, as shown here.")
    allure.dynamic.link("https://www.w3.org/TR/controller-document/#:~:text=The%20key%20words%20MAY%2C%20MUST%2C%20MUST%20NOT%2C%20OPTIONAL%2C%20RECOMMENDED%2C%20REQUIRED%2C%20and%20SHOULD%20in%20this%20document%20are%20to%20be%20interpreted%20as%20described%20in%20BCP%2014%20%5BRFC2119%5D%20%5BRFC8174%5D%20when%2C%20and%20only%20when%2C%20they%20appear%20in%20all%20capitals%2C%20as%20shown%20here.", name="Specification")
    allure.dynamic.parent_suite("Controller Documents 1.0")
    allure.dynamic.suite("00 Introduction")
    allure.dynamic.sub_suite("00 Conformance")
    pytest.skip("TBD")

def test_conformance_1():
    allure.dynamic.title("01 Conforming processors MUST produce errors when non-conforming documents are consumed.")
    allure.dynamic.link("https://www.w3.org/TR/controller-document/#:~:text=Conforming%20processors%20MUST%20produce%20errors%20when%20non%2Dconforming%20documents%20are%20consumed.", name="Specification")
    allure.dynamic.parent_suite("Controller Documents 1.0")
    allure.dynamic.suite("00 Introduction")
    allure.dynamic.sub_suite("00 Conformance")
    pytest.skip("TBD")

def test_controller_documents_0():
    allure.dynamic.title("00 The value of id MUST be a string that conforms to the rules in the URL Standard.")
    allure.dynamic.link("https://www.w3.org/TR/controller-document/#:~:text=The%20value%20of%20id%20MUST%20be%20a%20string%20that%20conforms%20to%20the%20rules%20in%20the%20URL%20Standard.", name="Specification")
    allure.dynamic.parent_suite("Controller Documents 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("00 Controller documents")
    pytest.skip("TBD")

def test_controller_documents_1():
    allure.dynamic.title("01 A controller document MUST contain an id value in the root map.")
    allure.dynamic.link("https://www.w3.org/TR/controller-document/#:~:text=A%20controller%20document%20MUST%20contain%20an%20id%20value%20in%20the%20root%20map.", name="Specification")
    allure.dynamic.parent_suite("Controller Documents 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("00 Controller documents")
    pytest.skip("TBD")

def test_controller_documents_2():
    allure.dynamic.title("02 If present, its value MUST be a string or a set of strings, each of which conforms to the rules in the URL Standard")
    allure.dynamic.link("https://www.w3.org/TR/controller-document/#:~:text=If%20present%2C%20its%20value%20MUST%20be%20a%20string%20or%20a%20set%20of%20strings%2C%20each%20of%20which%20conforms%20to%20the%20rules%20in%20the%20URL%20Standard", name="Specification")
    allure.dynamic.parent_suite("Controller Documents 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("00 Controller documents")
    pytest.skip("TBD")

def test_controller_documents_3():
    allure.dynamic.title("03 If the controller property is not present, the value expressed by the id property MUST be treated as if it were also set as the value of the controller property.")
    allure.dynamic.link("https://www.w3.org/TR/controller-document/#:~:text=If%20the%20controller%20property%20is%20not%20present%2C%20the%20value%20expressed%20by%20the%20id%20property%20MUST%20be%20treated%20as%20if%20it%20were%20also%20set%20as%20the%20value%20of%20the%20controller%20property.", name="Specification")
    allure.dynamic.parent_suite("Controller Documents 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("00 Controller documents")
    pytest.skip("TBD")

def test_controller_documents_4():
    allure.dynamic.title("04 If present, its value MUST be a set where each item in the set is a URI conforming to [RFC3986].")
    allure.dynamic.link("https://www.w3.org/TR/controller-document/#:~:text=If%20present%2C%20its%20value%20MUST%20be%20a%20set%20where%20each%20item%20in%20the%20set%20is%20a%20URI%20conforming%20to%20%5BRFC3986%5D.", name="Specification")
    allure.dynamic.parent_suite("Controller Documents 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("00 Controller documents")
    pytest.skip("TBD")

def test_verification_methods_0():
    allure.dynamic.title("00 If present, the value MUST be a set of verification methods, where each verification method is expressed using a map")
    allure.dynamic.link("https://www.w3.org/TR/controller-document/#:~:text=If%20present%2C%20the%20value%20MUST%20be%20a%20set%20of%20verification%20methods%2C%20where%20each%20verification%20method%20is%20expressed%20using%20a%20map", name="Specification")
    allure.dynamic.parent_suite("Controller Documents 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("01 Verification methods")
    pytest.skip("TBD")

def test_verification_methods_1():
    allure.dynamic.title("01 The verification method map MUST include the id, type, controller, and specific verification material properties that are determined by the value of type and are defined in 2.2.1 Verification Material")
    allure.dynamic.link("https://www.w3.org/TR/controller-document/#:~:text=The%20verification%20method%20map%20MUST%20include%20the%20id%2C%20type%2C%20controller%2C%20and%20specific%20verification%20material%20properties%20that%20are%20determined%20by%20the%20value%20of%20type%20and%20are%20defined%20in%202.2.1%20Verification%20Material", name="Specification")
    allure.dynamic.parent_suite("Controller Documents 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("01 Verification methods")
    pytest.skip("TBD")

def test_verification_methods_2():
    allure.dynamic.title("02 The value of the id property for a verification method MUST be a string that conforms to the [URL] syntax.")
    allure.dynamic.link("https://www.w3.org/TR/controller-document/#:~:text=The%20value%20of%20the%20id%20property%20for%20a%20verification%20method%20MUST%20be%20a%20string%20that%20conforms%20to%20the%20%5BURL%5D%20syntax.", name="Specification")
    allure.dynamic.parent_suite("Controller Documents 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("01 Verification methods")
    pytest.skip("TBD")

def test_verification_methods_3():
    allure.dynamic.title("03 The value of the type property MUST be a string that references exactly one verification method type.")
    allure.dynamic.link("https://www.w3.org/TR/controller-document/#:~:text=The%20value%20of%20the%20type%20property%20MUST%20be%20a%20string%20that%20references%20exactly%20one%20verification%20method%20type.", name="Specification")
    allure.dynamic.parent_suite("Controller Documents 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("01 Verification methods")
    pytest.skip("TBD")

def test_verification_methods_4():
    allure.dynamic.title("04 The value of the controller property MUST be a string that conforms to the [URL] syntax.")
    allure.dynamic.link("https://www.w3.org/TR/controller-document/#:~:text=The%20value%20of%20the%20controller%20property%20MUST%20be%20a%20string%20that%20conforms%20to%20the%20%5BURL%5D%20syntax.", name="Specification")
    allure.dynamic.parent_suite("Controller Documents 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("01 Verification methods")
    pytest.skip("TBD")

def test_verification_methods_5():
    allure.dynamic.title("05 If present, it MUST be an [XMLSCHEMA11-2] dateTimeStamp string specifying when the verification method SHOULD cease to be used")
    allure.dynamic.link("https://www.w3.org/TR/controller-document/#:~:text=If%20present%2C%20it%20MUST%20be%20an%20%5BXMLSCHEMA11%2D2%5D%20dateTimeStamp%20string%20specifying%20when%20the%20verification%20method%20SHOULD%20cease%20to%20be%20used", name="Specification")
    allure.dynamic.parent_suite("Controller Documents 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("01 Verification methods")
    pytest.skip("TBD")

def test_verification_methods_6():
    allure.dynamic.title("06 A verification method MUST NOT contain multiple verification material properties for the same material")
    allure.dynamic.link("https://www.w3.org/TR/controller-document/#:~:text=A%20verification%20method%20MUST%20NOT%20contain%20multiple%20verification%20material%20properties%20for%20the%20same%20material", name="Specification")
    allure.dynamic.parent_suite("Controller Documents 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("01 Verification methods")
    pytest.skip("TBD")

def test_verification_methods_7():
    allure.dynamic.title("07 As an internal implementation detail, such conversion MUST NOT affect the external representation of key material.")
    allure.dynamic.link("https://www.w3.org/TR/controller-document/#:~:text=As%20an%20internal%20implementation%20detail%2C%20such%20conversion%20MUST%20NOT%20affect%20the%20external%20representation%20of%20key%20material.", name="Specification")
    allure.dynamic.parent_suite("Controller Documents 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("01 Verification methods")
    pytest.skip("TBD")

def test_verification_methods_8():
    allure.dynamic.title("08 The value of the type property MUST contain the string Multikey.")
    allure.dynamic.link("https://www.w3.org/TR/controller-document/#:~:text=The%20value%20of%20the%20type%20property%20MUST%20contain%20the%20string%20Multikey.", name="Specification")
    allure.dynamic.parent_suite("Controller Documents 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("01 Verification methods")
    pytest.skip("TBD")

def test_verification_methods_9():
    allure.dynamic.title("09 If present, its value MUST be a Multibase encoded value as described in Section 2.4 Multibase.")
    allure.dynamic.link("https://www.w3.org/TR/controller-document/#:~:text=If%20present%2C%20its%20value%20MUST%20be%20a%20Multibase%20encoded%20value%20as%20described%20in%20Section%202.4%20Multibase.", name="Specification")
    allure.dynamic.parent_suite("Controller Documents 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("01 Verification methods")
    pytest.skip("TBD")

def test_verification_methods_10():
    allure.dynamic.title("10 The Multikey encoding of a P-256 public key MUST start with the two-byte prefix 0x8024 (the varint expression of 0x1200) followed by the 33-byte compressed public key data")
    allure.dynamic.link("https://www.w3.org/TR/controller-document/#:~:text=The%20Multikey%20encoding%20of%20a%20P%2D256%20public%20key%20MUST%20start%20with%20the%20two%2Dbyte%20prefix%200x8024%20%28the%20varint%20expression%20of%200x1200%29%20followed%20by%20the%2033%2Dbyte%20compressed%20public%20key%20data", name="Specification")
    allure.dynamic.parent_suite("Controller Documents 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("01 Verification methods")
    pytest.skip("TBD")

def test_verification_methods_11():
    allure.dynamic.title("11 The resulting 35-byte value MUST then be encoded using the base-58-btc alphabet, according to Section 2.4 Multibase, and then prepended with the base-58-btc Multibase header (z).")
    allure.dynamic.link("https://www.w3.org/TR/controller-document/#:~:text=The%20resulting%2035%2Dbyte%20value%20MUST%20then%20be%20encoded%20using%20the%20base%2D58%2Dbtc%20alphabet%2C%20according%20to%20Section%202.4%20Multibase%2C%20and%20then%20prepended%20with%20the%20base%2D58%2Dbtc%20Multibase%20header%20%28z%29.", name="Specification")
    allure.dynamic.parent_suite("Controller Documents 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("01 Verification methods")
    pytest.skip("TBD")

def test_verification_methods_12():
    allure.dynamic.title("12 The encoding of a P-384 public key MUST start with the two-byte prefix 0x8124 (the varint expression of 0x1201) followed by the 49-byte compressed public key data")
    allure.dynamic.link("https://www.w3.org/TR/controller-document/#:~:text=The%20encoding%20of%20a%20P%2D384%20public%20key%20MUST%20start%20with%20the%20two%2Dbyte%20prefix%200x8124%20%28the%20varint%20expression%20of%200x1201%29%20followed%20by%20the%2049%2Dbyte%20compressed%20public%20key%20data", name="Specification")
    allure.dynamic.parent_suite("Controller Documents 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("01 Verification methods")
    pytest.skip("TBD")

def test_verification_methods_13():
    allure.dynamic.title("13 The encoding of an Ed25519 public key MUST start with the two-byte prefix 0xed01 (the varint expression of 0xed), followed by the 32-byte public key data")
    allure.dynamic.link("https://www.w3.org/TR/controller-document/#:~:text=The%20encoding%20of%20an%20Ed25519%20public%20key%20MUST%20start%20with%20the%20two%2Dbyte%20prefix%200xed01%20%28the%20varint%20expression%20of%200xed%29%2C%20followed%20by%20the%2032%2Dbyte%20public%20key%20data", name="Specification")
    allure.dynamic.parent_suite("Controller Documents 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("01 Verification methods")
    pytest.skip("TBD")

def test_verification_methods_14():
    allure.dynamic.title("14 The resulting 34-byte value MUST then be encoded using the base-58-btc alphabet, according to Section 2.4 Multibase, and then prepended with the base-58-btc Multibase header (z).")
    allure.dynamic.link("https://www.w3.org/TR/controller-document/#:~:text=The%20resulting%2034%2Dbyte%20value%20MUST%20then%20be%20encoded%20using%20the%20base%2D58%2Dbtc%20alphabet%2C%20according%20to%20Section%202.4%20Multibase%2C%20and%20then%20prepended%20with%20the%20base%2D58%2Dbtc%20Multibase%20header%20%28z%29.", name="Specification")
    allure.dynamic.parent_suite("Controller Documents 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("01 Verification methods")
    pytest.skip("TBD")

def test_verification_methods_15():
    allure.dynamic.title("15 The encoding of an BLS12-381 public key in the G2 group MUST start with the two-byte prefix 0xeb01 (the varint expression of 0xeb), followed by the 96-byte compressed public key data")
    allure.dynamic.link("https://www.w3.org/TR/controller-document/#:~:text=The%20encoding%20of%20an%20BLS12%2D381%20public%20key%20in%20the%20G2%20group%20MUST%20start%20with%20the%20two%2Dbyte%20prefix%200xeb01%20%28the%20varint%20expression%20of%200xeb%29%2C%20followed%20by%20the%2096%2Dbyte%20compressed%20public%20key%20data", name="Specification")
    allure.dynamic.parent_suite("Controller Documents 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("01 Verification methods")
    pytest.skip("TBD")

def test_verification_methods_16():
    allure.dynamic.title("16 The resulting 98-byte value MUST then be encoded using the base-58-btc alphabet, according to Section 2.4 Multibase, and then prepended with the base-58-btc Multibase header (z).")
    allure.dynamic.link("https://www.w3.org/TR/controller-document/#:~:text=The%20resulting%2098%2Dbyte%20value%20MUST%20then%20be%20encoded%20using%20the%20base%2D58%2Dbtc%20alphabet%2C%20according%20to%20Section%202.4%20Multibase%2C%20and%20then%20prepended%20with%20the%20base%2D58%2Dbtc%20Multibase%20header%20%28z%29.", name="Specification")
    allure.dynamic.parent_suite("Controller Documents 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("01 Verification methods")
    pytest.skip("TBD")

def test_verification_methods_17():
    allure.dynamic.title("17 The Multikey encoding of a P-256 secret key MUST start with the two-byte prefix 0x8626 (the varint expression of 0x1306) followed by the 32-byte secret key data")
    allure.dynamic.link("https://www.w3.org/TR/controller-document/#:~:text=The%20Multikey%20encoding%20of%20a%20P%2D256%20secret%20key%20MUST%20start%20with%20the%20two%2Dbyte%20prefix%200x8626%20%28the%20varint%20expression%20of%200x1306%29%20followed%20by%20the%2032%2Dbyte%20secret%20key%20data", name="Specification")
    allure.dynamic.parent_suite("Controller Documents 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("01 Verification methods")
    pytest.skip("TBD")

def test_verification_methods_18():
    allure.dynamic.title("18 The encoding of a P-384 secret key MUST start with the two-byte prefix 0x8726 (the varint expression of 0x1307) followed by the 48-byte secret key data")
    allure.dynamic.link("https://www.w3.org/TR/controller-document/#:~:text=The%20encoding%20of%20a%20P%2D384%20secret%20key%20MUST%20start%20with%20the%20two%2Dbyte%20prefix%200x8726%20%28the%20varint%20expression%20of%200x1307%29%20followed%20by%20the%2048%2Dbyte%20secret%20key%20data", name="Specification")
    allure.dynamic.parent_suite("Controller Documents 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("01 Verification methods")
    pytest.skip("TBD")

def test_verification_methods_19():
    allure.dynamic.title("19 The encoding of an Ed25519 secret key MUST start with the two-byte prefix 0x8026 (the varint expression of 0x1300), followed by the 32-byte secret key data")
    allure.dynamic.link("https://www.w3.org/TR/controller-document/#:~:text=The%20encoding%20of%20an%20Ed25519%20secret%20key%20MUST%20start%20with%20the%20two%2Dbyte%20prefix%200x8026%20%28the%20varint%20expression%20of%200x1300%29%2C%20followed%20by%20the%2032%2Dbyte%20secret%20key%20data", name="Specification")
    allure.dynamic.parent_suite("Controller Documents 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("01 Verification methods")
    pytest.skip("TBD")

def test_verification_methods_20():
    allure.dynamic.title("20 The encoding of an BLS12-381 secret key in the G2 group MUST start with the two-byte prefix 0x8030 (the varint expression of 0x130a), followed by the 96-byte compressed public key data")
    allure.dynamic.link("https://www.w3.org/TR/controller-document/#:~:text=The%20encoding%20of%20an%20BLS12%2D381%20secret%20key%20in%20the%20G2%20group%20MUST%20start%20with%20the%20two%2Dbyte%20prefix%200x8030%20%28the%20varint%20expression%20of%200x130a%29%2C%20followed%20by%20the%2096%2Dbyte%20compressed%20public%20key%20data", name="Specification")
    allure.dynamic.parent_suite("Controller Documents 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("01 Verification methods")
    pytest.skip("TBD")

def test_verification_methods_21():
    allure.dynamic.title("21 When defining values for use with publicKeyMultibase and secretKeyMultibase, specification authors MAY define additional header values for other key types in other specifications and MUST NOT define alternate encodings for key types already defined by this specification.")
    allure.dynamic.link("https://www.w3.org/TR/controller-document/#:~:text=When%20defining%20values%20for%20use%20with%20publicKeyMultibase%20and%20secretKeyMultibase%2C%20specification%20authors%20MAY%20define%20additional%20header%20values%20for%20other%20key%20types%20in%20other%20specifications%20and%20MUST%20NOT%20define%20alternate%20encodings%20for%20key%20types%20already%20defined%20by%20this%20specification.", name="Specification")
    allure.dynamic.parent_suite("Controller Documents 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("01 Verification methods")
    pytest.skip("TBD")

def test_verification_methods_22():
    allure.dynamic.title("22 The value of the type property MUST contain the string JsonWebKey.")
    allure.dynamic.link("https://www.w3.org/TR/controller-document/#:~:text=The%20value%20of%20the%20type%20property%20MUST%20contain%20the%20string%20JsonWebKey.", name="Specification")
    allure.dynamic.parent_suite("Controller Documents 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("01 Verification methods")
    pytest.skip("TBD")

def test_verification_methods_23():
    allure.dynamic.title("23 If present, its value MUST be a map representing a JSON Web Key that conforms to [RFC7517]")
    allure.dynamic.link("https://www.w3.org/TR/controller-document/#:~:text=If%20present%2C%20its%20value%20MUST%20be%20a%20map%20representing%20a%20JSON%20Web%20Key%20that%20conforms%20to%20%5BRFC7517%5D", name="Specification")
    allure.dynamic.parent_suite("Controller Documents 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("01 Verification methods")
    pytest.skip("TBD")

def test_verification_methods_24():
    allure.dynamic.title("24 The map MUST NOT include any members of the private information class, such as d, as described in the JWK Registration Template")
    allure.dynamic.link("https://www.w3.org/TR/controller-document/#:~:text=The%20map%20MUST%20NOT%20include%20any%20members%20of%20the%20private%20information%20class%2C%20such%20as%20d%2C%20as%20described%20in%20the%20JWK%20Registration%20Template", name="Specification")
    allure.dynamic.parent_suite("Controller Documents 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("01 Verification methods")
    pytest.skip("TBD")

def test_verification_methods_25():
    allure.dynamic.title("25 As specified in Section 6.2.1.1 of the JWA specification, describing a key using an elliptic curve, the REQUIRED crv property is used to identify the particular curve type of the public key")
    allure.dynamic.link("https://www.w3.org/TR/controller-document/#:~:text=As%20specified%20in%20Section%206.2.1.1%20of%20the%20JWA%20specification%2C%20describing%20a%20key%20using%20an%20elliptic%20curve%2C%20the%20REQUIRED%20crv%20property%20is%20used%20to%20identify%20the%20particular%20curve%20type%20of%20the%20public%20key", name="Specification")
    allure.dynamic.parent_suite("Controller Documents 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("01 Verification methods")
    pytest.skip("TBD")

def test_verification_methods_26():
    allure.dynamic.title("26 It MUST NOT be used if the data structure containing it is public or may be revealed to parties other than the legitimate holders of the secret key.")
    allure.dynamic.link("https://www.w3.org/TR/controller-document/#:~:text=It%20MUST%20NOT%20be%20used%20if%20the%20data%20structure%20containing%20it%20is%20public%20or%20may%20be%20revealed%20to%20parties%20other%20than%20the%20legitimate%20holders%20of%20the%20secret%20key.", name="Specification")
    allure.dynamic.parent_suite("Controller Documents 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("01 Verification methods")
    pytest.skip("TBD")

def test_verification_methods_27():
    allure.dynamic.title("27 The publicKeyJwk property MUST NOT contain any property marked as 'Private' or 'Secret' in any registry contained in the JOSE Registries [JOSE-REGISTRIES], including 'd'.")
    allure.dynamic.link("https://www.w3.org/TR/controller-document/#:~:text=The%20publicKeyJwk%20property%20MUST%20NOT%20contain%20any%20property%20marked%20as%20%27Private%27%20or%20%27Secret%27%20in%20any%20registry%20contained%20in%20the%20JOSE%20Registries%20%5BJOSE%2DREGISTRIES%5D%2C%20including%20%27d%27.", name="Specification")
    allure.dynamic.parent_suite("Controller Documents 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("01 Verification methods")
    pytest.skip("TBD")

def test_verification_relationships_0():
    allure.dynamic.title("00 If present, its value MUST be a set of one or more verification methods")
    allure.dynamic.link("https://www.w3.org/TR/controller-document/#:~:text=If%20present%2C%20its%20value%20MUST%20be%20a%20set%20of%20one%20or%20more%20verification%20methods", name="Specification")
    allure.dynamic.parent_suite("Controller Documents 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("02 Verification relationships")
    pytest.skip("TBD")

def test_verification_relationships_1():
    allure.dynamic.title("01 If present, its associated value MUST be a set of one or more verification methods")
    allure.dynamic.link("https://www.w3.org/TR/controller-document/#:~:text=If%20present%2C%20its%20associated%20value%20MUST%20be%20a%20set%20of%20one%20or%20more%20verification%20methods", name="Specification")
    allure.dynamic.parent_suite("Controller Documents 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("02 Verification relationships")
    pytest.skip("TBD")

def test_verification_relationships_2():
    allure.dynamic.title("02 If present, the associated value MUST be a set of one or more verification methods")
    allure.dynamic.link("https://www.w3.org/TR/controller-document/#:~:text=If%20present%2C%20the%20associated%20value%20MUST%20be%20a%20set%20of%20one%20or%20more%20verification%20methods", name="Specification")
    allure.dynamic.parent_suite("Controller Documents 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("02 Verification relationships")
    pytest.skip("TBD")

def test_multibase_0_0():
    allure.dynamic.title("00 To base-encode a binary value into a Multibase string, an implementation MUST apply the algorithm in Section 3.1 Base Encode to the binary value, with the desired base encoding and alphabet from the table above, ensuring to prepend the associated Multibase header from the table above to the result")
    allure.dynamic.link("https://www.w3.org/TR/controller-document/#:~:text=To%20base%2Dencode%20a%20binary%20value%20into%20a%20Multibase%20string%2C%20an%20implementation%20MUST%20apply%20the%20algorithm%20in%20Section%203.1%20Base%20Encode%20to%20the%20binary%20value%2C%20with%20the%20desired%20base%20encoding%20and%20alphabet%20from%20the%20table%20above%2C%20ensuring%20to%20prepend%20the%20associated%20Multibase%20header%20from%20the%20table%20above%20to%20the%20result", name="Specification")
    allure.dynamic.parent_suite("Controller Documents 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("03 Multibase 0")
    pytest.skip("TBD")

def test_multibase_0_1():
    allure.dynamic.title("01 To base-decode a Multibase string, an implementation MUST apply the algorithm in Section 3.2 Base Decode to the string following the first character (Multibase header), with the alphabet associated with the Multibase header")
    allure.dynamic.link("https://www.w3.org/TR/controller-document/#:~:text=To%20base%2Ddecode%20a%20Multibase%20string%2C%20an%20implementation%20MUST%20apply%20the%20algorithm%20in%20Section%203.2%20Base%20Decode%20to%20the%20string%20following%20the%20first%20character%20%28Multibase%20header%29%2C%20with%20the%20alphabet%20associated%20with%20the%20Multibase%20header", name="Specification")
    allure.dynamic.parent_suite("Controller Documents 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("03 Multibase 0")
    pytest.skip("TBD")

def test_multihash_0():
    allure.dynamic.title("00 To encode to a Multihash value, an implementation MUST concatenate the associated Multihash header, the cryptographic hash length, and the cryptographic hash value, in that order.")
    allure.dynamic.link("https://www.w3.org/TR/controller-document/#:~:text=To%20encode%20to%20a%20Multihash%20value%2C%20an%20implementation%20MUST%20concatenate%20the%20associated%20Multihash%20header%2C%20the%20cryptographic%20hash%20length%2C%20and%20the%20cryptographic%20hash%20value%2C%20in%20that%20order.", name="Specification")
    allure.dynamic.parent_suite("Controller Documents 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("04 Multihash")
    pytest.skip("TBD")

def test_multihash_1():
    allure.dynamic.title("01 To decode a Multihash value, an implementation MUST 1) remove the prepended Multihash header value, which identifies the type of cryptographic hashing algorithm, 2) remove the output length, and 3) extract the raw cryptographic hash value which MUST match the expected output length associated with the Multihash header as well as the output length provided in the Multihash value itself.")
    allure.dynamic.link("https://www.w3.org/TR/controller-document/#:~:text=To%20decode%20a%20Multihash%20value%2C%20an%20implementation%20MUST%201%29%20remove%20the%20prepended%20Multihash%20header%20value%2C%20which%20identifies%20the%20type%20of%20cryptographic%20hashing%20algorithm%2C%202%29%20remove%20the%20output%20length%2C%20and%203%29%20extract%20the%20raw%20cryptographic%20hash%20value%20which%20MUST%20match%20the%20expected%20output%20length%20associated%20with%20the%20Multihash%20header%20as%20well%20as%20the%20output%20length%20provided%20in%20the%20Multihash%20value%20itself.", name="Specification")
    allure.dynamic.parent_suite("Controller Documents 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("04 Multihash")
    pytest.skip("TBD")

def test_base_encode_0():
    allure.dynamic.title("00 All mathematical operations MUST be performed using integer arithmetic")
    allure.dynamic.link("https://www.w3.org/TR/controller-document/#:~:text=All%20mathematical%20operations%20MUST%20be%20performed%20using%20integer%20arithmetic", name="Specification")
    allure.dynamic.parent_suite("Controller Documents 1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("00 Base encode")
    pytest.skip("TBD")

def test_base_decode_0():
    allure.dynamic.title("00 All mathematical operations MUST be performed using integer arithmetic")
    allure.dynamic.link("https://www.w3.org/TR/controller-document/#:~:text=All%20mathematical%20operations%20MUST%20be%20performed%20using%20integer%20arithmetic", name="Specification")
    allure.dynamic.parent_suite("Controller Documents 1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("01 Base decode")
    pytest.skip("TBD")

def test_retrieve_verification_method_0():
    allure.dynamic.title("00 If vmIdentifier is not a valid URL, an error MUST be raised and SHOULD convey an error type of INVALID_VERIFICATION_METHOD_URL.")
    allure.dynamic.link("https://www.w3.org/TR/controller-document/#:~:text=If%20vmIdentifier%20is%20not%20a%20valid%20URL%2C%20an%20error%20MUST%20be%20raised%20and%20SHOULD%20convey%20an%20error%20type%20of%20INVALID_VERIFICATION_METHOD_URL.", name="Specification")
    allure.dynamic.parent_suite("Controller Documents 1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("02 Retrieve verification method")
    pytest.skip("TBD")

def test_retrieve_verification_method_1():
    allure.dynamic.title("01 If controllerDocument.id does not match the controllerDocumentUrl, an error MUST be raised and SHOULD convey an error type of INVALID_CONTROLLER_DOCUMENT_ID.")
    allure.dynamic.link("https://www.w3.org/TR/controller-document/#:~:text=If%20controllerDocument.id%20does%20not%20match%20the%20controllerDocumentUrl%2C%20an%20error%20MUST%20be%20raised%20and%20SHOULD%20convey%20an%20error%20type%20of%20INVALID_CONTROLLER_DOCUMENT_ID.", name="Specification")
    allure.dynamic.parent_suite("Controller Documents 1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("02 Retrieve verification method")
    pytest.skip("TBD")

def test_retrieve_verification_method_2():
    allure.dynamic.title("02 If controllerDocument is not a conforming controller document, an error MUST be raised and SHOULD convey an error type of INVALID_CONTROLLER_DOCUMENT.")
    allure.dynamic.link("https://www.w3.org/TR/controller-document/#:~:text=If%20controllerDocument%20is%20not%20a%20conforming%20controller%20document%2C%20an%20error%20MUST%20be%20raised%20and%20SHOULD%20convey%20an%20error%20type%20of%20INVALID_CONTROLLER_DOCUMENT.", name="Specification")
    allure.dynamic.parent_suite("Controller Documents 1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("02 Retrieve verification method")
    pytest.skip("TBD")

def test_retrieve_verification_method_3():
    allure.dynamic.title("03 If verificationMethod is not a conforming verification method, an error MUST be raised and SHOULD convey an error type of INVALID_VERIFICATION_METHOD.")
    allure.dynamic.link("https://www.w3.org/TR/controller-document/#:~:text=If%20verificationMethod%20is%20not%20a%20conforming%20verification%20method%2C%20an%20error%20MUST%20be%20raised%20and%20SHOULD%20convey%20an%20error%20type%20of%20INVALID_VERIFICATION_METHOD.", name="Specification")
    allure.dynamic.parent_suite("Controller Documents 1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("02 Retrieve verification method")
    pytest.skip("TBD")

def test_retrieve_verification_method_4():
    allure.dynamic.title("04 If the verification method is not associated with a verification relationship array in the controllerDocument, either by reference (URL) or by value (object), an error MUST be raised and SHOULD convey an error type of INVALID_RELATIONSHIP_FOR_VERIFICATION_METHOD.")
    allure.dynamic.link("https://www.w3.org/TR/controller-document/#:~:text=If%20the%20verification%20method%20is%20not%20associated%20with%20a%20verification%20relationship%20array%20in%20the%20controllerDocument%2C%20either%20by%20reference%20%28URL%29%20or%20by%20value%20%28object%29%2C%20an%20error%20MUST%20be%20raised%20and%20SHOULD%20convey%20an%20error%20type%20of%20INVALID_RELATIONSHIP_FOR_VERIFICATION_METHOD.", name="Specification")
    allure.dynamic.parent_suite("Controller Documents 1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("02 Retrieve verification method")
    pytest.skip("TBD")

def test_processing_errors_0():
    allure.dynamic.title("00 The type value of the error object MUST be a URL that starts with the value https://w3id.org/security# and ends with the value in the section listed below.")
    allure.dynamic.link("https://www.w3.org/TR/controller-document/#:~:text=The%20type%20value%20of%20the%20error%20object%20MUST%20be%20a%20URL%20that%20starts%20with%20the%20value%20https%3A//w3id.org/security%23%20and%20ends%20with%20the%20value%20in%20the%20section%20listed%20below.", name="Specification")
    allure.dynamic.parent_suite("Controller Documents 1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("03 Processing errors")
    pytest.skip("TBD")

def test_processing_errors_1():
    allure.dynamic.title("01 The code value MUST be the integer code described in the table below (in parentheses, beside the type name).")
    allure.dynamic.link("https://www.w3.org/TR/controller-document/#:~:text=The%20code%20value%20MUST%20be%20the%20integer%20code%20described%20in%20the%20table%20below%20%28in%20parentheses%2C%20beside%20the%20type%20name%29.", name="Specification")
    allure.dynamic.parent_suite("Controller Documents 1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("03 Processing errors")
    pytest.skip("TBD")

def test_context_injection_0():
    allure.dynamic.title("00 If an @context property is not provided in a document that is being secured or verified, or any Data Integrity terms used in the document are not mapped by existing values in the @context property, implementations using JSON-LD MUST inject or add an @context property with a value of https://www.w3.org/ns/controller/v1.")
    allure.dynamic.link("https://www.w3.org/TR/controller-document/#:~:text=If%20an%20%40context%20property%20is%20not%20provided%20in%20a%20document%20that%20is%20being%20secured%20or%20verified%2C%20or%20any%20Data%20Integrity%20terms%20used%20in%20the%20document%20are%20not%20mapped%20by%20existing%20values%20in%20the%20%40context%20property%2C%20implementations%20using%20JSON%2DLD%20MUST%20inject%20or%20add%20an%20%40context%20property%20with%20a%20value%20of%20https%3A//www.w3.org/ns/controller/v1.", name="Specification")
    allure.dynamic.parent_suite("Controller Documents 1.0")
    allure.dynamic.suite("03 Contexts and vocabularies")
    allure.dynamic.sub_suite("00 Context injection")
    pytest.skip("TBD")
