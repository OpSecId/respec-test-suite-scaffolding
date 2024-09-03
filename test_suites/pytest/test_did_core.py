import allure
import pytest

def test_conformance_0():
    allure.dynamic.title("00 The key words MAY, MUST, MUST NOT, OPTIONAL, RECOMMENDED, REQUIRED, SHOULD, and SHOULD NOT in this document are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all capitals, as shown here.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=The%20key%20words%20MAY%2C%20MUST%2C%20MUST%20NOT%2C%20OPTIONAL%2C%20RECOMMENDED%2C%20REQUIRED%2C%20SHOULD%2C%20and%20SHOULD%20NOT%20in%20this%20document%20are%20to%20be%20interpreted%20as%20described%20in%20BCP%2014%20%5BRFC2119%5D%20%5BRFC8174%5D%20when%2C%20and%20only%20when%2C%20they%20appear%20in%20all%20capitals%2C%20as%20shown%20here.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("00 Introduction")
    allure.dynamic.sub_suite("00 Conformance")
    pytest.skip("TBD")

def test_did_syntax_0():
    allure.dynamic.title("00 All DIDs MUST conform to the DID Syntax ABNF Rules.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=All%20DIDs%20MUST%20conform%20to%20the%20DID%20Syntax%20ABNF%20Rules.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("01 Identifier")
    allure.dynamic.sub_suite("00 Did syntax")
    pytest.skip("TBD")

def test_did_url_syntax_0():
    allure.dynamic.title("00 All DID URLs MUST conform to the DID URL Syntax ABNF Rules")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=All%20DID%20URLs%20MUST%20conform%20to%20the%20DID%20URL%20Syntax%20ABNF%20Rules", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("01 Identifier")
    allure.dynamic.sub_suite("01 Did url syntax")
    pytest.skip("TBD")

def test_did_url_syntax_1():
    allure.dynamic.title("01 If present, the associated value MUST be an ASCII string.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=If%20present%2C%20the%20associated%20value%20MUST%20be%20an%20ASCII%20string.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("01 Identifier")
    allure.dynamic.sub_suite("01 Did url syntax")
    pytest.skip("TBD")

def test_did_url_syntax_2():
    allure.dynamic.title("02 If present, the associated value MUST be an ASCII string and MUST use percent-encoding for certain characters as specified in RFC3986 Section 2.1.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=If%20present%2C%20the%20associated%20value%20MUST%20be%20an%20ASCII%20string%20and%20MUST%20use%20percent%2Dencoding%20for%20certain%20characters%20as%20specified%20in%20RFC3986%20Section%202.1.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("01 Identifier")
    allure.dynamic.sub_suite("01 Did url syntax")
    pytest.skip("TBD")

def test_did_url_syntax_3():
    allure.dynamic.title("03 If present, the associated value MUST be an ASCII string which is a valid XML datetime value, as defined in section 3.3.7 of W3C XML Schema Definition Language (XSD) 1.1 Part 2: Datatypes [XMLSCHEMA11-2]")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=If%20present%2C%20the%20associated%20value%20MUST%20be%20an%20ASCII%20string%20which%20is%20a%20valid%20XML%20datetime%20value%2C%20as%20defined%20in%20section%203.3.7%20of%20W3C%20XML%20Schema%20Definition%20Language%20%28XSD%29%201.1%20Part%202%3A%20Datatypes%20%5BXMLSCHEMA11%2D2%5D", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("01 Identifier")
    allure.dynamic.sub_suite("01 Did url syntax")
    pytest.skip("TBD")

def test_did_url_syntax_4():
    allure.dynamic.title("04 This datetime value MUST be normalized to UTC 00:00:00 and without sub-second decimal precision")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=This%20datetime%20value%20MUST%20be%20normalized%20to%20UTC%2000%3A00%3A00%20and%20without%20sub%2Dsecond%20decimal%20precision", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("01 Identifier")
    allure.dynamic.sub_suite("01 Did url syntax")
    pytest.skip("TBD")

def test_did_url_syntax_5():
    allure.dynamic.title("05 When resolving a relative DID URL reference, the algorithm specified in RFC3986 Section 5: Reference Resolution MUST be used")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=When%20resolving%20a%20relative%20DID%20URL%20reference%2C%20the%20algorithm%20specified%20in%20RFC3986%20Section%205%3A%20Reference%20Resolution%20MUST%20be%20used", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("01 Identifier")
    allure.dynamic.sub_suite("01 Did url syntax")
    pytest.skip("TBD")

def test_identifiers_0():
    allure.dynamic.title("00 The value of id MUST be a string that conforms to the rules in 3.1 DID Syntax and MUST exist in the root map of the data model for the DID document.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=The%20value%20of%20id%20MUST%20be%20a%20string%20that%20conforms%20to%20the%20rules%20in%203.1%20DID%20Syntax%20and%20MUST%20exist%20in%20the%20root%20map%20of%20the%20data%20model%20for%20the%20DID%20document.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("02 Core properties")
    allure.dynamic.sub_suite("00 Identifiers")
    pytest.skip("TBD")

def test_identifiers_1():
    allure.dynamic.title("01 If present, the value MUST be a string or a set of strings that conform to the rules in 3.1 DID Syntax")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=If%20present%2C%20the%20value%20MUST%20be%20a%20string%20or%20a%20set%20of%20strings%20that%20conform%20to%20the%20rules%20in%203.1%20DID%20Syntax", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("02 Core properties")
    allure.dynamic.sub_suite("00 Identifiers")
    pytest.skip("TBD")

def test_identifiers_2():
    allure.dynamic.title("02 If present, the value MUST be a set where each item in the set is a URI conforming to [RFC3986].")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=If%20present%2C%20the%20value%20MUST%20be%20a%20set%20where%20each%20item%20in%20the%20set%20is%20a%20URI%20conforming%20to%20%5BRFC3986%5D.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("02 Core properties")
    allure.dynamic.sub_suite("00 Identifiers")
    pytest.skip("TBD")

def test_verification_methods_0():
    allure.dynamic.title("00 If present, the value MUST be a set of verification methods, where each verification method is expressed using a map")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=If%20present%2C%20the%20value%20MUST%20be%20a%20set%20of%20verification%20methods%2C%20where%20each%20verification%20method%20is%20expressed%20using%20a%20map", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("02 Core properties")
    allure.dynamic.sub_suite("01 Verification methods")
    pytest.skip("TBD")

def test_verification_methods_1():
    allure.dynamic.title("01 The verification method map MUST include the id, type, controller, and specific verification material properties that are determined by the value of type and are defined in 5.2.1 Verification Material")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=The%20verification%20method%20map%20MUST%20include%20the%20id%2C%20type%2C%20controller%2C%20and%20specific%20verification%20material%20properties%20that%20are%20determined%20by%20the%20value%20of%20type%20and%20are%20defined%20in%205.2.1%20Verification%20Material", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("02 Core properties")
    allure.dynamic.sub_suite("01 Verification methods")
    pytest.skip("TBD")

def test_verification_methods_2():
    allure.dynamic.title("02 The value of the id property for a verification method MUST be a string that conforms to the rules in Section 3.2 DID URL Syntax.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=The%20value%20of%20the%20id%20property%20for%20a%20verification%20method%20MUST%20be%20a%20string%20that%20conforms%20to%20the%20rules%20in%20Section%203.2%20DID%20URL%20Syntax.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("02 Core properties")
    allure.dynamic.sub_suite("01 Verification methods")
    pytest.skip("TBD")

def test_verification_methods_3():
    allure.dynamic.title("03 The value of the type property MUST be a string that references exactly one verification method type")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=The%20value%20of%20the%20type%20property%20MUST%20be%20a%20string%20that%20references%20exactly%20one%20verification%20method%20type", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("02 Core properties")
    allure.dynamic.sub_suite("01 Verification methods")
    pytest.skip("TBD")

def test_verification_methods_4():
    allure.dynamic.title("04 The value of the controller property MUST be a string that conforms to the rules in 3.1 DID Syntax.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=The%20value%20of%20the%20controller%20property%20MUST%20be%20a%20string%20that%20conforms%20to%20the%20rules%20in%203.1%20DID%20Syntax.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("02 Core properties")
    allure.dynamic.sub_suite("01 Verification methods")
    pytest.skip("TBD")

def test_verification_methods_5():
    allure.dynamic.title("05 If present, the value MUST be a map representing a JSON Web Key that conforms to [RFC7517]")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=If%20present%2C%20the%20value%20MUST%20be%20a%20map%20representing%20a%20JSON%20Web%20Key%20that%20conforms%20to%20%5BRFC7517%5D", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("02 Core properties")
    allure.dynamic.sub_suite("01 Verification methods")
    pytest.skip("TBD")

def test_verification_methods_6():
    allure.dynamic.title("06 The map MUST NOT contain 'd', or any other members of the private information class as described in Registration Template")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=The%20map%20MUST%20NOT%20contain%20%27d%27%2C%20or%20any%20other%20members%20of%20the%20private%20information%20class%20as%20described%20in%20Registration%20Template", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("02 Core properties")
    allure.dynamic.sub_suite("01 Verification methods")
    pytest.skip("TBD")

def test_verification_methods_7():
    allure.dynamic.title("07 If present, the value MUST be a string representation of a [MULTIBASE] encoded public key.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=If%20present%2C%20the%20value%20MUST%20be%20a%20string%20representation%20of%20a%20%5BMULTIBASE%5D%20encoded%20public%20key.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("02 Core properties")
    allure.dynamic.sub_suite("01 Verification methods")
    pytest.skip("TBD")

def test_verification_methods_8():
    allure.dynamic.title("08 A verification method MUST NOT contain multiple verification material properties for the same material")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=A%20verification%20method%20MUST%20NOT%20contain%20multiple%20verification%20material%20properties%20for%20the%20same%20material", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("02 Core properties")
    allure.dynamic.sub_suite("01 Verification methods")
    pytest.skip("TBD")

def test_verification_relationships_0():
    allure.dynamic.title("00 If present, the associated value MUST be a set of one or more verification methods")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=If%20present%2C%20the%20associated%20value%20MUST%20be%20a%20set%20of%20one%20or%20more%20verification%20methods", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("02 Core properties")
    allure.dynamic.sub_suite("02 Verification relationships")
    pytest.skip("TBD")

def test_services_0():
    allure.dynamic.title("00 If present, the associated value MUST be a set of services, where each service is described by a map")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=If%20present%2C%20the%20associated%20value%20MUST%20be%20a%20set%20of%20services%2C%20where%20each%20service%20is%20described%20by%20a%20map", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("02 Core properties")
    allure.dynamic.sub_suite("03 Services")
    pytest.skip("TBD")

def test_services_1():
    allure.dynamic.title("01 Each service map MUST contain id, type, and serviceEndpoint properties")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=Each%20service%20map%20MUST%20contain%20id%2C%20type%2C%20and%20serviceEndpoint%20properties", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("02 Core properties")
    allure.dynamic.sub_suite("03 Services")
    pytest.skip("TBD")

def test_services_2():
    allure.dynamic.title("02 The value of the id property MUST be a URI conforming to [RFC3986]")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=The%20value%20of%20the%20id%20property%20MUST%20be%20a%20URI%20conforming%20to%20%5BRFC3986%5D", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("02 Core properties")
    allure.dynamic.sub_suite("03 Services")
    pytest.skip("TBD")

def test_services_3():
    allure.dynamic.title("03 A conforming producer MUST NOT produce multiple service entries with the same id")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=A%20conforming%20producer%20MUST%20NOT%20produce%20multiple%20service%20entries%20with%20the%20same%20id", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("02 Core properties")
    allure.dynamic.sub_suite("03 Services")
    pytest.skip("TBD")

def test_services_4():
    allure.dynamic.title("04 A conforming consumer MUST produce an error if it detects multiple service entries with the same id.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=A%20conforming%20consumer%20MUST%20produce%20an%20error%20if%20it%20detects%20multiple%20service%20entries%20with%20the%20same%20id.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("02 Core properties")
    allure.dynamic.sub_suite("03 Services")
    pytest.skip("TBD")

def test_services_5():
    allure.dynamic.title("05 The value of the type property MUST be a string or a set of strings")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=The%20value%20of%20the%20type%20property%20MUST%20be%20a%20string%20or%20a%20set%20of%20strings", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("02 Core properties")
    allure.dynamic.sub_suite("03 Services")
    pytest.skip("TBD")

def test_services_6():
    allure.dynamic.title("06 The value of the serviceEndpoint property MUST be a string, a map, or a set composed of one or more strings and/or maps")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=The%20value%20of%20the%20serviceEndpoint%20property%20MUST%20be%20a%20string%2C%20a%20map%2C%20or%20a%20set%20composed%20of%20one%20or%20more%20strings%20and/or%20maps", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("02 Core properties")
    allure.dynamic.sub_suite("03 Services")
    pytest.skip("TBD")

def test_services_7():
    allure.dynamic.title("07 All string values MUST be valid URIs conforming to [RFC3986] and normalized according to the Normalization and Comparison rules in RFC3986 and to any normalization rules in its applicable URI scheme specification.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=All%20string%20values%20MUST%20be%20valid%20URIs%20conforming%20to%20%5BRFC3986%5D%20and%20normalized%20according%20to%20the%20Normalization%20and%20Comparison%20rules%20in%20RFC3986%20and%20to%20any%20normalization%20rules%20in%20its%20applicable%20URI%20scheme%20specification.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("02 Core properties")
    allure.dynamic.sub_suite("03 Services")
    pytest.skip("TBD")

def test_production_and_consumption_0():
    allure.dynamic.title("00 A representation MUST define deterministic production and consumption rules for all data types specified in 4")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=A%20representation%20MUST%20define%20deterministic%20production%20and%20consumption%20rules%20for%20all%20data%20types%20specified%20in%204", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("03 Representations")
    allure.dynamic.sub_suite("00 Production and consumption")
    pytest.skip("TBD")

def test_production_and_consumption_1():
    allure.dynamic.title("01 A representation MUST be uniquely associated with an IANA-registered Media Type.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=A%20representation%20MUST%20be%20uniquely%20associated%20with%20an%20IANA%2Dregistered%20Media%20Type.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("03 Representations")
    allure.dynamic.sub_suite("00 Production and consumption")
    pytest.skip("TBD")

def test_production_and_consumption_2():
    allure.dynamic.title("02 A representation MUST define fragment processing rules for its Media Type that are conformant with the fragment processing rules defined in Fragment.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=A%20representation%20MUST%20define%20fragment%20processing%20rules%20for%20its%20Media%20Type%20that%20are%20conformant%20with%20the%20fragment%20processing%20rules%20defined%20in%20Fragment.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("03 Representations")
    allure.dynamic.sub_suite("00 Production and consumption")
    pytest.skip("TBD")

def test_production_and_consumption_3():
    allure.dynamic.title("03 A conforming producer MUST take a DID document data model and a representation-specific entries map as input into the production process")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=A%20conforming%20producer%20MUST%20take%20a%20DID%20document%20data%20model%20and%20a%20representation%2Dspecific%20entries%20map%20as%20input%20into%20the%20production%20process", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("03 Representations")
    allure.dynamic.sub_suite("00 Production and consumption")
    pytest.skip("TBD")

def test_production_and_consumption_4():
    allure.dynamic.title("04 A conforming producer MUST serialize all entries in the DID document data model, and the representation-specific entries map, that do not have explicit processing rules for the representation being produced using only the representation's data type processing rules and return the serialization after the production process completes.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=A%20conforming%20producer%20MUST%20serialize%20all%20entries%20in%20the%20DID%20document%20data%20model%2C%20and%20the%20representation%2Dspecific%20entries%20map%2C%20that%20do%20not%20have%20explicit%20processing%20rules%20for%20the%20representation%20being%20produced%20using%20only%20the%20representation%27s%20data%20type%20processing%20rules%20and%20return%20the%20serialization%20after%20the%20production%20process%20completes.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("03 Representations")
    allure.dynamic.sub_suite("00 Production and consumption")
    pytest.skip("TBD")

def test_production_and_consumption_5():
    allure.dynamic.title("05 A conforming producer MUST return the Media Type string associated with the representation after the production process completes.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=A%20conforming%20producer%20MUST%20return%20the%20Media%20Type%20string%20associated%20with%20the%20representation%20after%20the%20production%20process%20completes.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("03 Representations")
    allure.dynamic.sub_suite("00 Production and consumption")
    pytest.skip("TBD")

def test_production_and_consumption_6():
    allure.dynamic.title("06 A conforming producer MUST NOT produce non-conforming DIDs or DID documents.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=A%20conforming%20producer%20MUST%20NOT%20produce%20non%2Dconforming%20DIDs%20or%20DID%20documents.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("03 Representations")
    allure.dynamic.sub_suite("00 Production and consumption")
    pytest.skip("TBD")

def test_production_and_consumption_7():
    allure.dynamic.title("07 A conforming consumer MUST take a representation and Media Type string as input into the consumption process")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=A%20conforming%20consumer%20MUST%20take%20a%20representation%20and%20Media%20Type%20string%20as%20input%20into%20the%20consumption%20process", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("03 Representations")
    allure.dynamic.sub_suite("00 Production and consumption")
    pytest.skip("TBD")

def test_production_and_consumption_8():
    allure.dynamic.title("08 A conforming consumer MUST determine the representation of a DID document using the Media Type input string.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=A%20conforming%20consumer%20MUST%20determine%20the%20representation%20of%20a%20DID%20document%20using%20the%20Media%20Type%20input%20string.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("03 Representations")
    allure.dynamic.sub_suite("00 Production and consumption")
    pytest.skip("TBD")

def test_production_and_consumption_9():
    allure.dynamic.title("09 A conforming consumer MUST detect any representation-specific entry across all known representations and place the entry into a representation-specific entries map which is returned after the consumption process completes")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=A%20conforming%20consumer%20MUST%20detect%20any%20representation%2Dspecific%20entry%20across%20all%20known%20representations%20and%20place%20the%20entry%20into%20a%20representation%2Dspecific%20entries%20map%20which%20is%20returned%20after%20the%20consumption%20process%20completes", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("03 Representations")
    allure.dynamic.sub_suite("00 Production and consumption")
    pytest.skip("TBD")

def test_production_and_consumption_10():
    allure.dynamic.title("10 A conforming consumer MUST add all non-representation-specific entries that do not have explicit processing rules for the representation being consumed to the DID document data model using only the representation's data type processing rules and return the DID document data model after the consumption process completes.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=A%20conforming%20consumer%20MUST%20add%20all%20non%2Drepresentation%2Dspecific%20entries%20that%20do%20not%20have%20explicit%20processing%20rules%20for%20the%20representation%20being%20consumed%20to%20the%20DID%20document%20data%20model%20using%20only%20the%20representation%27s%20data%20type%20processing%20rules%20and%20return%20the%20DID%20document%20data%20model%20after%20the%20consumption%20process%20completes.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("03 Representations")
    allure.dynamic.sub_suite("00 Production and consumption")
    pytest.skip("TBD")

def test_production_and_consumption_11():
    allure.dynamic.title("11 A conforming consumer MUST produce errors when consuming non-conforming DIDs or DID documents.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=A%20conforming%20consumer%20MUST%20produce%20errors%20when%20consuming%20non%2Dconforming%20DIDs%20or%20DID%20documents.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("03 Representations")
    allure.dynamic.sub_suite("00 Production and consumption")
    pytest.skip("TBD")

def test_json_0():
    allure.dynamic.title("00 The DID document, DID document data structures, and representation-specific entries map MUST be serialized to the JSON representation according to the following production rules:")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=The%20DID%20document%2C%20DID%20document%20data%20structures%2C%20and%20representation%2Dspecific%20entries%20map%20MUST%20be%20serialized%20to%20the%20JSON%20representation%20according%20to%20the%20following%20production%20rules%3A", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("03 Representations")
    allure.dynamic.sub_suite("01 Json")
    pytest.skip("TBD")

def test_json_1():
    allure.dynamic.title("01 All entries of a DID document MUST be included in the root JSON Object")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=All%20entries%20of%20a%20DID%20document%20MUST%20be%20included%20in%20the%20root%20JSON%20Object", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("03 Representations")
    allure.dynamic.sub_suite("01 Json")
    pytest.skip("TBD")

def test_json_2():
    allure.dynamic.title("02 When serializing a DID document, a conforming producer MUST specify a media type of application/did+json to downstream applications such as described in 7.1.2 DID Resolution Metadata.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=When%20serializing%20a%20DID%20document%2C%20a%20conforming%20producer%20MUST%20specify%20a%20media%20type%20of%20application/did%2Bjson%20to%20downstream%20applications%20such%20as%20described%20in%207.1.2%20DID%20Resolution%20Metadata.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("03 Representations")
    allure.dynamic.sub_suite("01 Json")
    pytest.skip("TBD")

def test_json_3():
    allure.dynamic.title("03 The DID document and DID document data structures JSON representation MUST be deserialized into the data model according to the following consumption rules:")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=The%20DID%20document%20and%20DID%20document%20data%20structures%20JSON%20representation%20MUST%20be%20deserialized%20into%20the%20data%20model%20according%20to%20the%20following%20consumption%20rules%3A", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("03 Representations")
    allure.dynamic.sub_suite("01 Json")
    pytest.skip("TBD")

def test_json_4():
    allure.dynamic.title("04 If media type information is available to a conforming consumer and the media type value is application/did+json, then the data structure being consumed is a DID document, and the root element MUST be a JSON Object where all members of the object are entries of the DID document")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=If%20media%20type%20information%20is%20available%20to%20a%20conforming%20consumer%20and%20the%20media%20type%20value%20is%20application/did%2Bjson%2C%20then%20the%20data%20structure%20being%20consumed%20is%20a%20DID%20document%2C%20and%20the%20root%20element%20MUST%20be%20a%20JSON%20Object%20where%20all%20members%20of%20the%20object%20are%20entries%20of%20the%20DID%20document", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("03 Representations")
    allure.dynamic.sub_suite("01 Json")
    pytest.skip("TBD")

def test_json_5():
    allure.dynamic.title("05 A conforming consumer for a JSON representation that is consuming a DID document with a root element that is not a JSON Object MUST report an error.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=A%20conforming%20consumer%20for%20a%20JSON%20representation%20that%20is%20consuming%20a%20DID%20document%20with%20a%20root%20element%20that%20is%20not%20a%20JSON%20Object%20MUST%20report%20an%20error.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("03 Representations")
    allure.dynamic.sub_suite("01 Json")
    pytest.skip("TBD")

def test_json_ld_0():
    allure.dynamic.title("00 The DID document, DID document data structures, and representation-specific entries map MUST be serialized to the JSON-LD representation according to the JSON representation production rules as defined in 6.2 JSON.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=The%20DID%20document%2C%20DID%20document%20data%20structures%2C%20and%20representation%2Dspecific%20entries%20map%20MUST%20be%20serialized%20to%20the%20JSON%2DLD%20representation%20according%20to%20the%20JSON%20representation%20production%20rules%20as%20defined%20in%206.2%20JSON.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("03 Representations")
    allure.dynamic.sub_suite("02 Json ld")
    pytest.skip("TBD")

def test_json_ld_1():
    allure.dynamic.title("01 In addition to using the JSON representation production rules, JSON-LD production MUST include the representation-specific @context entry")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=In%20addition%20to%20using%20the%20JSON%20representation%20production%20rules%2C%20JSON%2DLD%20production%20MUST%20include%20the%20representation%2Dspecific%20%40context%20entry", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("03 Representations")
    allure.dynamic.sub_suite("02 Json ld")
    pytest.skip("TBD")

def test_json_ld_2():
    allure.dynamic.title("02 The serialized value of @context MUST be the JSON String https://www.w3.org/ns/did/v1, or a JSON Array where the first item is the JSON String https://www.w3.org/ns/did/v1 and the subsequent items are serialized according to the JSON representation production rules.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=The%20serialized%20value%20of%20%40context%20MUST%20be%20the%20JSON%20String%20https%3A//www.w3.org/ns/did/v1%2C%20or%20a%20JSON%20Array%20where%20the%20first%20item%20is%20the%20JSON%20String%20https%3A//www.w3.org/ns/did/v1%20and%20the%20subsequent%20items%20are%20serialized%20according%20to%20the%20JSON%20representation%20production%20rules.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("03 Representations")
    allure.dynamic.sub_suite("02 Json ld")
    pytest.skip("TBD")

def test_json_ld_3():
    allure.dynamic.title("03 When serializing a JSON-LD representation of a DID document, a conforming producer MUST specify a media type of application/did+ld+json to downstream applications such as described in 7.1.2 DID Resolution Metadata.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=When%20serializing%20a%20JSON%2DLD%20representation%20of%20a%20DID%20document%2C%20a%20conforming%20producer%20MUST%20specify%20a%20media%20type%20of%20application/did%2Bld%2Bjson%20to%20downstream%20applications%20such%20as%20described%20in%207.1.2%20DID%20Resolution%20Metadata.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("03 Representations")
    allure.dynamic.sub_suite("02 Json ld")
    pytest.skip("TBD")

def test_json_ld_4():
    allure.dynamic.title("04 The DID document and any DID document data structures expressed by a JSON-LD representation MUST be deserialized into the data model according to the JSON representation consumption rules as defined in 6.2 JSON.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=The%20DID%20document%20and%20any%20DID%20document%20data%20structures%20expressed%20by%20a%20JSON%2DLD%20representation%20MUST%20be%20deserialized%20into%20the%20data%20model%20according%20to%20the%20JSON%20representation%20consumption%20rules%20as%20defined%20in%206.2%20JSON.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("03 Representations")
    allure.dynamic.sub_suite("02 Json ld")
    pytest.skip("TBD")

def test_did_resolution_0():
    allure.dynamic.title("00 This input is REQUIRED and the value MUST be a conformant DID as defined in 3.1 DID Syntax.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=This%20input%20is%20REQUIRED%20and%20the%20value%20MUST%20be%20a%20conformant%20DID%20as%20defined%20in%203.1%20DID%20Syntax.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("04 Resolution")
    allure.dynamic.sub_suite("00 Did resolution")
    pytest.skip("TBD")

def test_did_resolution_1():
    allure.dynamic.title("01 This input is REQUIRED, but the structure MAY be empty.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=This%20input%20is%20REQUIRED%2C%20but%20the%20structure%20MAY%20be%20empty.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("04 Resolution")
    allure.dynamic.sub_suite("00 Did resolution")
    pytest.skip("TBD")

def test_did_resolution_2():
    allure.dynamic.title("02 This structure is REQUIRED, and in the case of an error in the resolution process, this MUST NOT be empty")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=This%20structure%20is%20REQUIRED%2C%20and%20in%20the%20case%20of%20an%20error%20in%20the%20resolution%20process%2C%20this%20MUST%20NOT%20be%20empty", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("04 Resolution")
    allure.dynamic.sub_suite("00 Did resolution")
    pytest.skip("TBD")

def test_did_resolution_3():
    allure.dynamic.title("03 If resolveRepresentation was called, this structure MUST contain a contentType property containing the Media Type of the representation found in the didDocumentStream")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=If%20resolveRepresentation%20was%20called%2C%20this%20structure%20MUST%20contain%20a%20contentType%20property%20containing%20the%20Media%20Type%20of%20the%20representation%20found%20in%20the%20didDocumentStream", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("04 Resolution")
    allure.dynamic.sub_suite("00 Did resolution")
    pytest.skip("TBD")

def test_did_resolution_4():
    allure.dynamic.title("04 If the resolution is not successful, this structure MUST contain an error property describing the error.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=If%20the%20resolution%20is%20not%20successful%2C%20this%20structure%20MUST%20contain%20an%20error%20property%20describing%20the%20error.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("04 Resolution")
    allure.dynamic.sub_suite("00 Did resolution")
    pytest.skip("TBD")

def test_did_resolution_5():
    allure.dynamic.title("05 If the resolution is successful, and if the resolve function was called, this MUST be a DID document abstract data model (a map) as described in 4")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=If%20the%20resolution%20is%20successful%2C%20and%20if%20the%20resolve%20function%20was%20called%2C%20this%20MUST%20be%20a%20DID%20document%20abstract%20data%20model%20%28a%20map%29%20as%20described%20in%204", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("04 Resolution")
    allure.dynamic.sub_suite("00 Did resolution")
    pytest.skip("TBD")

def test_did_resolution_6():
    allure.dynamic.title("06 The value of id in the resolved DID document MUST match the DID that was resolved")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=The%20value%20of%20id%20in%20the%20resolved%20DID%20document%20MUST%20match%20the%20DID%20that%20was%20resolved", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("04 Resolution")
    allure.dynamic.sub_suite("00 Did resolution")
    pytest.skip("TBD")

def test_did_resolution_7():
    allure.dynamic.title("07 If the resolution is unsuccessful, this value MUST be empty.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=If%20the%20resolution%20is%20unsuccessful%2C%20this%20value%20MUST%20be%20empty.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("04 Resolution")
    allure.dynamic.sub_suite("00 Did resolution")
    pytest.skip("TBD")

def test_did_resolution_8():
    allure.dynamic.title("08 If the resolution is successful, and if the resolveRepresentation function was called, this MUST be a byte stream of the resolved DID document in one of the conformant representations")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=If%20the%20resolution%20is%20successful%2C%20and%20if%20the%20resolveRepresentation%20function%20was%20called%2C%20this%20MUST%20be%20a%20byte%20stream%20of%20the%20resolved%20DID%20document%20in%20one%20of%20the%20conformant%20representations", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("04 Resolution")
    allure.dynamic.sub_suite("00 Did resolution")
    pytest.skip("TBD")

def test_did_resolution_9():
    allure.dynamic.title("09 If the resolution is unsuccessful, this value MUST be an empty stream.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=If%20the%20resolution%20is%20unsuccessful%2C%20this%20value%20MUST%20be%20an%20empty%20stream.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("04 Resolution")
    allure.dynamic.sub_suite("00 Did resolution")
    pytest.skip("TBD")

def test_did_resolution_10():
    allure.dynamic.title("10 If the resolution is successful, this MUST be a metadata structure")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=If%20the%20resolution%20is%20successful%2C%20this%20MUST%20be%20a%20metadata%20structure", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("04 Resolution")
    allure.dynamic.sub_suite("00 Did resolution")
    pytest.skip("TBD")

def test_did_resolution_11():
    allure.dynamic.title("11 If the resolution is unsuccessful, this output MUST be an empty metadata structure")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=If%20the%20resolution%20is%20unsuccessful%2C%20this%20output%20MUST%20be%20an%20empty%20metadata%20structure", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("04 Resolution")
    allure.dynamic.sub_suite("00 Did resolution")
    pytest.skip("TBD")

def test_did_resolution_12():
    allure.dynamic.title("12 The Media Type MUST be expressed as an ASCII string")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=The%20Media%20Type%20MUST%20be%20expressed%20as%20an%20ASCII%20string", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("04 Resolution")
    allure.dynamic.sub_suite("00 Did resolution")
    pytest.skip("TBD")

def test_did_resolution_13():
    allure.dynamic.title("13 This property is OPTIONAL for the resolveRepresentation function and MUST NOT be used with the resolve function.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=This%20property%20is%20OPTIONAL%20for%20the%20resolveRepresentation%20function%20and%20MUST%20NOT%20be%20used%20with%20the%20resolve%20function.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("04 Resolution")
    allure.dynamic.sub_suite("00 Did resolution")
    pytest.skip("TBD")

def test_did_resolution_14():
    allure.dynamic.title("14 This property is REQUIRED if resolution is successful and if the resolveRepresentation function was called")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=This%20property%20is%20REQUIRED%20if%20resolution%20is%20successful%20and%20if%20the%20resolveRepresentation%20function%20was%20called", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("04 Resolution")
    allure.dynamic.sub_suite("00 Did resolution")
    pytest.skip("TBD")

def test_did_resolution_15():
    allure.dynamic.title("15 This property MUST NOT be present if the resolve function was called")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=This%20property%20MUST%20NOT%20be%20present%20if%20the%20resolve%20function%20was%20called", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("04 Resolution")
    allure.dynamic.sub_suite("00 Did resolution")
    pytest.skip("TBD")

def test_did_resolution_16():
    allure.dynamic.title("16 The value of this property MUST be an ASCII string that is the Media Type of the conformant representations")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=The%20value%20of%20this%20property%20MUST%20be%20an%20ASCII%20string%20that%20is%20the%20Media%20Type%20of%20the%20conformant%20representations", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("04 Resolution")
    allure.dynamic.sub_suite("00 Did resolution")
    pytest.skip("TBD")

def test_did_resolution_17():
    allure.dynamic.title("17 The caller of the resolveRepresentation function MUST use this value when determining how to parse and process the didDocumentStream returned by this function into the data model.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=The%20caller%20of%20the%20resolveRepresentation%20function%20MUST%20use%20this%20value%20when%20determining%20how%20to%20parse%20and%20process%20the%20didDocumentStream%20returned%20by%20this%20function%20into%20the%20data%20model.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("04 Resolution")
    allure.dynamic.sub_suite("00 Did resolution")
    pytest.skip("TBD")

def test_did_resolution_18():
    allure.dynamic.title("18 This property is REQUIRED when there is an error in the resolution process")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=This%20property%20is%20REQUIRED%20when%20there%20is%20an%20error%20in%20the%20resolution%20process", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("04 Resolution")
    allure.dynamic.sub_suite("00 Did resolution")
    pytest.skip("TBD")

def test_did_resolution_19():
    allure.dynamic.title("19 The value of this property MUST be a single keyword ASCII string")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=The%20value%20of%20this%20property%20MUST%20be%20a%20single%20keyword%20ASCII%20string", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("04 Resolution")
    allure.dynamic.sub_suite("00 Did resolution")
    pytest.skip("TBD")

def test_did_resolution_20():
    allure.dynamic.title("20 The value of the property MUST be a string formatted as an XML Datetime normalized to UTC 00:00:00 and without sub-second decimal precision")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=The%20value%20of%20the%20property%20MUST%20be%20a%20string%20formatted%20as%20an%20XML%20Datetime%20normalized%20to%20UTC%2000%3A00%3A00%20and%20without%20sub%2Dsecond%20decimal%20precision", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("04 Resolution")
    allure.dynamic.sub_suite("00 Did resolution")
    pytest.skip("TBD")

def test_did_resolution_21():
    allure.dynamic.title("21 The value of the property MUST follow the same formatting rules as the created property")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=The%20value%20of%20the%20property%20MUST%20follow%20the%20same%20formatting%20rules%20as%20the%20created%20property", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("04 Resolution")
    allure.dynamic.sub_suite("00 Did resolution")
    pytest.skip("TBD")

def test_did_resolution_22():
    allure.dynamic.title("22 If a DID has been deactivated, DID document metadata MUST include this property with the boolean value true")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=If%20a%20DID%20has%20been%20deactivated%2C%20DID%20document%20metadata%20MUST%20include%20this%20property%20with%20the%20boolean%20value%20true", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("04 Resolution")
    allure.dynamic.sub_suite("00 Did resolution")
    pytest.skip("TBD")

def test_did_resolution_23():
    allure.dynamic.title("23 If a DID has not been deactivated, this property is OPTIONAL, but if included, MUST have the boolean value false.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=If%20a%20DID%20has%20not%20been%20deactivated%2C%20this%20property%20is%20OPTIONAL%2C%20but%20if%20included%2C%20MUST%20have%20the%20boolean%20value%20false.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("04 Resolution")
    allure.dynamic.sub_suite("00 Did resolution")
    pytest.skip("TBD")

def test_did_resolution_24():
    allure.dynamic.title("24 The value of the property MUST follow the same formatting rules as the created property.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=The%20value%20of%20the%20property%20MUST%20follow%20the%20same%20formatting%20rules%20as%20the%20created%20property.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("04 Resolution")
    allure.dynamic.sub_suite("00 Did resolution")
    pytest.skip("TBD")

def test_did_resolution_25():
    allure.dynamic.title("25 The value of the property MUST be an ASCII string.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=The%20value%20of%20the%20property%20MUST%20be%20an%20ASCII%20string.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("04 Resolution")
    allure.dynamic.sub_suite("00 Did resolution")
    pytest.skip("TBD")

def test_did_resolution_26():
    allure.dynamic.title("26 If present, the value MUST be a set where each item is a string that conforms to the rules in Section 3.1 DID Syntax")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=If%20present%2C%20the%20value%20MUST%20be%20a%20set%20where%20each%20item%20is%20a%20string%20that%20conforms%20to%20the%20rules%20in%20Section%203.1%20DID%20Syntax", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("04 Resolution")
    allure.dynamic.sub_suite("00 Did resolution")
    pytest.skip("TBD")

def test_did_resolution_27():
    allure.dynamic.title("27 Each equivalentId DID value MUST be produced by, and a form of, the same DID method as the id property value")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=Each%20equivalentId%20DID%20value%20MUST%20be%20produced%20by%2C%20and%20a%20form%20of%2C%20the%20same%20DID%20method%20as%20the%20id%20property%20value", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("04 Resolution")
    allure.dynamic.sub_suite("00 Did resolution")
    pytest.skip("TBD")

def test_did_resolution_28():
    allure.dynamic.title("28 A conforming DID method specification MUST guarantee that each equivalentId value is logically equivalent to the id property value.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=A%20conforming%20DID%20method%20specification%20MUST%20guarantee%20that%20each%20equivalentId%20value%20is%20logically%20equivalent%20to%20the%20id%20property%20value.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("04 Resolution")
    allure.dynamic.sub_suite("00 Did resolution")
    pytest.skip("TBD")

def test_did_resolution_29():
    allure.dynamic.title("29 equivalentId is a much stronger form of equivalence than alsoKnownAs because the equivalence MUST be guaranteed by the governing DID method")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=equivalentId%20is%20a%20much%20stronger%20form%20of%20equivalence%20than%20alsoKnownAs%20because%20the%20equivalence%20MUST%20be%20guaranteed%20by%20the%20governing%20DID%20method", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("04 Resolution")
    allure.dynamic.sub_suite("00 Did resolution")
    pytest.skip("TBD")

def test_did_resolution_30():
    allure.dynamic.title("30 If present, the value MUST be a string that conforms to the rules in Section 3.1 DID Syntax")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=If%20present%2C%20the%20value%20MUST%20be%20a%20string%20that%20conforms%20to%20the%20rules%20in%20Section%203.1%20DID%20Syntax", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("04 Resolution")
    allure.dynamic.sub_suite("00 Did resolution")
    pytest.skip("TBD")

def test_did_resolution_31():
    allure.dynamic.title("31 A canonicalId value MUST be produced by, and a form of, the same DID method as the id property value")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=A%20canonicalId%20value%20MUST%20be%20produced%20by%2C%20and%20a%20form%20of%2C%20the%20same%20DID%20method%20as%20the%20id%20property%20value", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("04 Resolution")
    allure.dynamic.sub_suite("00 Did resolution")
    pytest.skip("TBD")

def test_did_resolution_32():
    allure.dynamic.title("32 A conforming DID method specification MUST guarantee that the canonicalId value is logically equivalent to the id property value.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=A%20conforming%20DID%20method%20specification%20MUST%20guarantee%20that%20the%20canonicalId%20value%20is%20logically%20equivalent%20to%20the%20id%20property%20value.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("04 Resolution")
    allure.dynamic.sub_suite("00 Did resolution")
    pytest.skip("TBD")

def test_did_url_dereferencing_0():
    allure.dynamic.title("00 To dereference a DID fragment, the complete DID URL including the DID fragment MUST be used")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=To%20dereference%20a%20DID%20fragment%2C%20the%20complete%20DID%20URL%20including%20the%20DID%20fragment%20MUST%20be%20used", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("04 Resolution")
    allure.dynamic.sub_suite("01 Did url dereferencing")
    pytest.skip("TBD")

def test_did_url_dereferencing_1():
    allure.dynamic.title("01 This input is REQUIRED")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=This%20input%20is%20REQUIRED", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("04 Resolution")
    allure.dynamic.sub_suite("01 Did url dereferencing")
    pytest.skip("TBD")

def test_did_url_dereferencing_2():
    allure.dynamic.title("02 This input is REQUIRED, but the structure MAY be empty.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=This%20input%20is%20REQUIRED%2C%20but%20the%20structure%20MAY%20be%20empty.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("04 Resolution")
    allure.dynamic.sub_suite("01 Did url dereferencing")
    pytest.skip("TBD")

def test_did_url_dereferencing_3():
    allure.dynamic.title("03 This structure is REQUIRED, and in the case of an error in the dereferencing process, this MUST NOT be empty")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=This%20structure%20is%20REQUIRED%2C%20and%20in%20the%20case%20of%20an%20error%20in%20the%20dereferencing%20process%2C%20this%20MUST%20NOT%20be%20empty", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("04 Resolution")
    allure.dynamic.sub_suite("01 Did url dereferencing")
    pytest.skip("TBD")

def test_did_url_dereferencing_4():
    allure.dynamic.title("04 If the dereferencing is not successful, this structure MUST contain an error property describing the error.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=If%20the%20dereferencing%20is%20not%20successful%2C%20this%20structure%20MUST%20contain%20an%20error%20property%20describing%20the%20error.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("04 Resolution")
    allure.dynamic.sub_suite("01 Did url dereferencing")
    pytest.skip("TBD")

def test_did_url_dereferencing_5():
    allure.dynamic.title("05 If the dereferencing function was called and successful, this MUST contain a resource corresponding to the DID URL")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=If%20the%20dereferencing%20function%20was%20called%20and%20successful%2C%20this%20MUST%20contain%20a%20resource%20corresponding%20to%20the%20DID%20URL", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("04 Resolution")
    allure.dynamic.sub_suite("01 Did url dereferencing")
    pytest.skip("TBD")

def test_did_url_dereferencing_6():
    allure.dynamic.title("06 If the dereferencing is unsuccessful, this value MUST be empty.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=If%20the%20dereferencing%20is%20unsuccessful%2C%20this%20value%20MUST%20be%20empty.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("04 Resolution")
    allure.dynamic.sub_suite("01 Did url dereferencing")
    pytest.skip("TBD")

def test_did_url_dereferencing_7():
    allure.dynamic.title("07 If the dereferencing is successful, this MUST be a metadata structure, but the structure MAY be empty")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=If%20the%20dereferencing%20is%20successful%2C%20this%20MUST%20be%20a%20metadata%20structure%2C%20but%20the%20structure%20MAY%20be%20empty", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("04 Resolution")
    allure.dynamic.sub_suite("01 Did url dereferencing")
    pytest.skip("TBD")

def test_did_url_dereferencing_8():
    allure.dynamic.title("08 If the contentStream is a DID document, this MUST be a didDocumentMetadata structure as described in DID Resolution")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=If%20the%20contentStream%20is%20a%20DID%20document%2C%20this%20MUST%20be%20a%20didDocumentMetadata%20structure%20as%20described%20in%20DID%20Resolution", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("04 Resolution")
    allure.dynamic.sub_suite("01 Did url dereferencing")
    pytest.skip("TBD")

def test_did_url_dereferencing_9():
    allure.dynamic.title("09 If the dereferencing is unsuccessful, this output MUST be an empty metadata structure.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=If%20the%20dereferencing%20is%20unsuccessful%2C%20this%20output%20MUST%20be%20an%20empty%20metadata%20structure.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("04 Resolution")
    allure.dynamic.sub_suite("01 Did url dereferencing")
    pytest.skip("TBD")

def test_did_url_dereferencing_10():
    allure.dynamic.title("10 The Media Type MUST be expressed as an ASCII string")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=The%20Media%20Type%20MUST%20be%20expressed%20as%20an%20ASCII%20string", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("04 Resolution")
    allure.dynamic.sub_suite("01 Did url dereferencing")
    pytest.skip("TBD")

def test_did_url_dereferencing_11():
    allure.dynamic.title("11 The Media Type value MUST be expressed as an ASCII string.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=The%20Media%20Type%20value%20MUST%20be%20expressed%20as%20an%20ASCII%20string.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("04 Resolution")
    allure.dynamic.sub_suite("01 Did url dereferencing")
    pytest.skip("TBD")

def test_did_url_dereferencing_12():
    allure.dynamic.title("12 This property is REQUIRED when there is an error in the dereferencing process")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=This%20property%20is%20REQUIRED%20when%20there%20is%20an%20error%20in%20the%20dereferencing%20process", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("04 Resolution")
    allure.dynamic.sub_suite("01 Did url dereferencing")
    pytest.skip("TBD")

def test_did_url_dereferencing_13():
    allure.dynamic.title("13 The value of this property MUST be a single keyword expressed as an ASCII string")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=The%20value%20of%20this%20property%20MUST%20be%20a%20single%20keyword%20expressed%20as%20an%20ASCII%20string", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("04 Resolution")
    allure.dynamic.sub_suite("01 Did url dereferencing")
    pytest.skip("TBD")

def test_metadata_structure_0():
    allure.dynamic.title("00 The structure used to communicate this metadata MUST be a map of properties")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=The%20structure%20used%20to%20communicate%20this%20metadata%20MUST%20be%20a%20map%20of%20properties", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("04 Resolution")
    allure.dynamic.sub_suite("02 Metadata structure")
    pytest.skip("TBD")

def test_metadata_structure_1():
    allure.dynamic.title("01 Each property name MUST be a string")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=Each%20property%20name%20MUST%20be%20a%20string", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("04 Resolution")
    allure.dynamic.sub_suite("02 Metadata structure")
    pytest.skip("TBD")

def test_metadata_structure_2():
    allure.dynamic.title("02 Each property value MUST be a string, map, list, set, boolean, or null")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=Each%20property%20value%20MUST%20be%20a%20string%2C%20map%2C%20list%2C%20set%2C%20boolean%2C%20or%20null", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("04 Resolution")
    allure.dynamic.sub_suite("02 Metadata structure")
    pytest.skip("TBD")

def test_metadata_structure_3():
    allure.dynamic.title("03 The values within any complex data structures such as maps and lists MUST be one of these data types as well")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=The%20values%20within%20any%20complex%20data%20structures%20such%20as%20maps%20and%20lists%20MUST%20be%20one%20of%20these%20data%20types%20as%20well", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("04 Resolution")
    allure.dynamic.sub_suite("02 Metadata structure")
    pytest.skip("TBD")

def test_metadata_structure_4():
    allure.dynamic.title("04 All metadata property definitions registered in the DID Specification Registries [DID-SPEC-REGISTRIES] MUST define the value type, including any additional formats or restrictions to that value (for example, a string formatted as a date or as a decimal integer)")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=All%20metadata%20property%20definitions%20registered%20in%20the%20DID%20Specification%20Registries%20%5BDID%2DSPEC%2DREGISTRIES%5D%20MUST%20define%20the%20value%20type%2C%20including%20any%20additional%20formats%20or%20restrictions%20to%20that%20value%20%28for%20example%2C%20a%20string%20formatted%20as%20a%20date%20or%20as%20a%20decimal%20integer%29", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("04 Resolution")
    allure.dynamic.sub_suite("02 Metadata structure")
    pytest.skip("TBD")

def test_metadata_structure_5():
    allure.dynamic.title("05 The entire metadata structure MUST be serializable according to the JSON serialization rules in the [INFRA] specification")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=The%20entire%20metadata%20structure%20MUST%20be%20serializable%20according%20to%20the%20JSON%20serialization%20rules%20in%20the%20%5BINFRA%5D%20specification", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("04 Resolution")
    allure.dynamic.sub_suite("02 Metadata structure")
    pytest.skip("TBD")

def test_method_syntax_0():
    allure.dynamic.title("00 A DID method specification MUST define exactly one method-specific DID scheme that is identified by exactly one method name as specified by the method-name rule in 3.1 DID Syntax.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=A%20DID%20method%20specification%20MUST%20define%20exactly%20one%20method%2Dspecific%20DID%20scheme%20that%20is%20identified%20by%20exactly%20one%20method%20name%20as%20specified%20by%20the%20method%2Dname%20rule%20in%203.1%20DID%20Syntax.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("05 Methods")
    allure.dynamic.sub_suite("00 Method syntax")
    pytest.skip("TBD")

def test_method_syntax_1():
    allure.dynamic.title("01 The DID method specification MUST specify how to generate the method-specific-id component of a DID.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=The%20DID%20method%20specification%20MUST%20specify%20how%20to%20generate%20the%20method%2Dspecific%2Did%20component%20of%20a%20DID.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("05 Methods")
    allure.dynamic.sub_suite("00 Method syntax")
    pytest.skip("TBD")

def test_method_syntax_2():
    allure.dynamic.title("02 The DID method specification MUST define sensitivity and normalization of the value of the method-specific-id.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=The%20DID%20method%20specification%20MUST%20define%20sensitivity%20and%20normalization%20of%20the%20value%20of%20the%20method%2Dspecific%2Did.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("05 Methods")
    allure.dynamic.sub_suite("00 Method syntax")
    pytest.skip("TBD")

def test_method_syntax_3():
    allure.dynamic.title("03 The method-specific-id value MUST be unique within a DID method")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=The%20method%2Dspecific%2Did%20value%20MUST%20be%20unique%20within%20a%20DID%20method", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("05 Methods")
    allure.dynamic.sub_suite("00 Method syntax")
    pytest.skip("TBD")

def test_method_syntax_4():
    allure.dynamic.title("04 Any DID generated by a DID method MUST be globally unique.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=Any%20DID%20generated%20by%20a%20DID%20method%20MUST%20be%20globally%20unique.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("05 Methods")
    allure.dynamic.sub_suite("00 Method syntax")
    pytest.skip("TBD")

def test_method_syntax_5():
    allure.dynamic.title("05 The use of colons MUST comply syntactically with the method-specific-id ABNF rule.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=The%20use%20of%20colons%20MUST%20comply%20syntactically%20with%20the%20method%2Dspecific%2Did%20ABNF%20rule.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("05 Methods")
    allure.dynamic.sub_suite("00 Method syntax")
    pytest.skip("TBD")

def test_method_operations_0():
    allure.dynamic.title("00 A DID method specification MUST define how authorization is performed to execute all operations, including any necessary cryptographic processes.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=A%20DID%20method%20specification%20MUST%20define%20how%20authorization%20is%20performed%20to%20execute%20all%20operations%2C%20including%20any%20necessary%20cryptographic%20processes.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("05 Methods")
    allure.dynamic.sub_suite("01 Method operations")
    pytest.skip("TBD")

def test_method_operations_1():
    allure.dynamic.title("01 A DID method specification MUST specify how a DID controller creates a DID and its associated DID document.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=A%20DID%20method%20specification%20MUST%20specify%20how%20a%20DID%20controller%20creates%20a%20DID%20and%20its%20associated%20DID%20document.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("05 Methods")
    allure.dynamic.sub_suite("01 Method operations")
    pytest.skip("TBD")

def test_method_operations_2():
    allure.dynamic.title("02 A DID method specification MUST specify how a DID resolver uses a DID to resolve a DID document, including how the DID resolver can verify the authenticity of the response.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=A%20DID%20method%20specification%20MUST%20specify%20how%20a%20DID%20resolver%20uses%20a%20DID%20to%20resolve%20a%20DID%20document%2C%20including%20how%20the%20DID%20resolver%20can%20verify%20the%20authenticity%20of%20the%20response.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("05 Methods")
    allure.dynamic.sub_suite("01 Method operations")
    pytest.skip("TBD")

def test_method_operations_3():
    allure.dynamic.title("03 A DID method specification MUST specify what constitutes an update to a DID document and how a DID controller can update a DID document or state that updates are not possible.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=A%20DID%20method%20specification%20MUST%20specify%20what%20constitutes%20an%20update%20to%20a%20DID%20document%20and%20how%20a%20DID%20controller%20can%20update%20a%20DID%20document%20or%20state%20that%20updates%20are%20not%20possible.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("05 Methods")
    allure.dynamic.sub_suite("01 Method operations")
    pytest.skip("TBD")

def test_method_operations_4():
    allure.dynamic.title("04 The DID method specification MUST specify how a DID controller can deactivate a DID or state that deactivation is not possible.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=The%20DID%20method%20specification%20MUST%20specify%20how%20a%20DID%20controller%20can%20deactivate%20a%20DID%20or%20state%20that%20deactivation%20is%20not%20possible.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("05 Methods")
    allure.dynamic.sub_suite("01 Method operations")
    pytest.skip("TBD")

def test_security_requirements_0():
    allure.dynamic.title("00 A DID method specifications MUST follow all guidelines and normative language provided in RFC3552: Writing Security Considerations Sections for the DID operations defined in the DID method specification.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=A%20DID%20method%20specifications%20MUST%20follow%20all%20guidelines%20and%20normative%20language%20provided%20in%20RFC3552%3A%20Writing%20Security%20Considerations%20Sections%20for%20the%20DID%20operations%20defined%20in%20the%20DID%20method%20specification.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("05 Methods")
    allure.dynamic.sub_suite("02 Security requirements")
    pytest.skip("TBD")

def test_security_requirements_1():
    allure.dynamic.title("01 The Security Considerations section MUST document the following forms of attack for the DID operations defined in the DID method specification: eavesdropping, replay, message insertion, deletion, modification, denial of service, amplification, and man-in-the-middle")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=The%20Security%20Considerations%20section%20MUST%20document%20the%20following%20forms%20of%20attack%20for%20the%20DID%20operations%20defined%20in%20the%20DID%20method%20specification%3A%20eavesdropping%2C%20replay%2C%20message%20insertion%2C%20deletion%2C%20modification%2C%20denial%20of%20service%2C%20amplification%2C%20and%20man%2Din%2Dthe%2Dmiddle", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("05 Methods")
    allure.dynamic.sub_suite("02 Security requirements")
    pytest.skip("TBD")

def test_security_requirements_2():
    allure.dynamic.title("02 The Security Considerations section MUST discuss residual risks, such as the risks from compromise in a related protocol, incorrect implementation, or cipher after threat mitigation was deployed.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=The%20Security%20Considerations%20section%20MUST%20discuss%20residual%20risks%2C%20such%20as%20the%20risks%20from%20compromise%20in%20a%20related%20protocol%2C%20incorrect%20implementation%2C%20or%20cipher%20after%20threat%20mitigation%20was%20deployed.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("05 Methods")
    allure.dynamic.sub_suite("02 Security requirements")
    pytest.skip("TBD")

def test_security_requirements_3():
    allure.dynamic.title("03 The Security Considerations section MUST provide integrity protection and update authentication for all operations required by Section 8.2 Method Operations.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=The%20Security%20Considerations%20section%20MUST%20provide%20integrity%20protection%20and%20update%20authentication%20for%20all%20operations%20required%20by%20Section%208.2%20Method%20Operations.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("05 Methods")
    allure.dynamic.sub_suite("02 Security requirements")
    pytest.skip("TBD")

def test_security_requirements_4():
    allure.dynamic.title("04 If authentication is involved, particularly user-host authentication, the security characteristics of the authentication method MUST be clearly documented.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=If%20authentication%20is%20involved%2C%20particularly%20user%2Dhost%20authentication%2C%20the%20security%20characteristics%20of%20the%20authentication%20method%20MUST%20be%20clearly%20documented.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("05 Methods")
    allure.dynamic.sub_suite("02 Security requirements")
    pytest.skip("TBD")

def test_security_requirements_5():
    allure.dynamic.title("05 The Security Considerations section MUST discuss the policy mechanism by which DIDs are proven to be uniquely assigned.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=The%20Security%20Considerations%20section%20MUST%20discuss%20the%20policy%20mechanism%20by%20which%20DIDs%20are%20proven%20to%20be%20uniquely%20assigned.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("05 Methods")
    allure.dynamic.sub_suite("02 Security requirements")
    pytest.skip("TBD")

def test_security_requirements_6():
    allure.dynamic.title("06 Method-specific endpoint authentication MUST be discussed")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=Method%2Dspecific%20endpoint%20authentication%20MUST%20be%20discussed", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("05 Methods")
    allure.dynamic.sub_suite("02 Security requirements")
    pytest.skip("TBD")

def test_security_requirements_7():
    allure.dynamic.title("07 Where DID methods make use of DLTs with varying network topology, sometimes offered as light node or thin client implementations to reduce required computing resources, the security assumptions of the topology available to implementations of the DID method MUST be discussed.")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=Where%20DID%20methods%20make%20use%20of%20DLTs%20with%20varying%20network%20topology%2C%20sometimes%20offered%20as%20light%20node%20or%20thin%20client%20implementations%20to%20reduce%20required%20computing%20resources%2C%20the%20security%20assumptions%20of%20the%20topology%20available%20to%20implementations%20of%20the%20DID%20method%20MUST%20be%20discussed.", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("05 Methods")
    allure.dynamic.sub_suite("02 Security requirements")
    pytest.skip("TBD")

def test_security_requirements_8():
    allure.dynamic.title("08 If a protocol incorporates cryptographic protection mechanisms, the DID method specification MUST clearly indicate which portions of the data are protected and by what protections, and it SHOULD give an indication of the sorts of attacks to which the cryptographic protection is susceptible")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=If%20a%20protocol%20incorporates%20cryptographic%20protection%20mechanisms%2C%20the%20DID%20method%20specification%20MUST%20clearly%20indicate%20which%20portions%20of%20the%20data%20are%20protected%20and%20by%20what%20protections%2C%20and%20it%20SHOULD%20give%20an%20indication%20of%20the%20sorts%20of%20attacks%20to%20which%20the%20cryptographic%20protection%20is%20susceptible", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("05 Methods")
    allure.dynamic.sub_suite("02 Security requirements")
    pytest.skip("TBD")

def test_privacy_requirements_0():
    allure.dynamic.title("00 The DID method specification's Privacy Considerations section MUST discuss any subsection of Section 5 of [RFC6973] that could apply in a method-specific manner")
    allure.dynamic.link("https://www.w3.org/TR/did-core/#:~:text=The%20DID%20method%20specification%27s%20Privacy%20Considerations%20section%20MUST%20discuss%20any%20subsection%20of%20Section%205%20of%20%5BRFC6973%5D%20that%20could%20apply%20in%20a%20method%2Dspecific%20manner", name="Specification")
    allure.dynamic.parent_suite("Decentralized Identifiers (DIDs) v1.0")
    allure.dynamic.suite("05 Methods")
    allure.dynamic.sub_suite("03 Privacy requirements")
    pytest.skip("TBD")
