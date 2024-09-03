import allure
import pytest

def test_conformance_0():
    allure.dynamic.title("00 The key words MAY, MUST, MUST NOT, RECOMMENDED, and SHOULD in this document are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all capitals, as shown here.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=The%20key%20words%20MAY%2C%20MUST%2C%20MUST%20NOT%2C%20RECOMMENDED%2C%20and%20SHOULD%20in%20this%20document%20are%20to%20be%20interpreted%20as%20described%20in%20BCP%2014%20%5BRFC2119%5D%20%5BRFC8174%5D%20when%2C%20and%20only%20when%2C%20they%20appear%20in%20all%20capitals%2C%20as%20shown%20here.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("00 Introduction")
    allure.dynamic.sub_suite("00 Conformance")
    pytest.skip("TBD")

def test_conformance_1():
    allure.dynamic.title("01 Syntaxes of this document MUST be enforced")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=Syntaxes%20of%20this%20document%20MUST%20be%20enforced", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("00 Introduction")
    allure.dynamic.sub_suite("00 Conformance")
    pytest.skip("TBD")

def test_conformance_2():
    allure.dynamic.title("02 A serialization format for the conforming document MUST be deterministic, bi-directional, and lossless as described in Section 6")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=A%20serialization%20format%20for%20the%20conforming%20document%20MUST%20be%20deterministic%2C%20bi%2Ddirectional%2C%20and%20lossless%20as%20described%20in%20Section%206", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("00 Introduction")
    allure.dynamic.sub_suite("00 Conformance")
    pytest.skip("TBD")

def test_conformance_3():
    allure.dynamic.title("03 Conforming processors MUST produce errors when non-conforming documents are consumed.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=Conforming%20processors%20MUST%20produce%20errors%20when%20non%2Dconforming%20documents%20are%20consumed.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("00 Introduction")
    allure.dynamic.sub_suite("00 Conformance")
    pytest.skip("TBD")

def test_contexts_0():
    allure.dynamic.title("00 Verifiable credentials and verifiable presentations MUST include a @context property.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=Verifiable%20credentials%20and%20verifiable%20presentations%20MUST%20include%20a%20%40context%20property.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("00 Contexts")
    pytest.skip("TBD")

def test_contexts_1():
    allure.dynamic.title("01 The value of the @context property MUST be an ordered set where the first item is a URI with the value https://www.w3.org/2018/credentials/v1")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=The%20value%20of%20the%20%40context%20property%20MUST%20be%20an%20ordered%20set%20where%20the%20first%20item%20is%20a%20URI%20with%20the%20value%20https%3A//www.w3.org/2018/credentials/v1", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("00 Contexts")
    pytest.skip("TBD")

def test_contexts_2():
    allure.dynamic.title("02 Subsequent items in the array MUST express context information and be composed of any combination of URIs or objects")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=Subsequent%20items%20in%20the%20array%20MUST%20express%20context%20information%20and%20be%20composed%20of%20any%20combination%20of%20URIs%20or%20objects", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("00 Contexts")
    pytest.skip("TBD")

def test_contexts_3():
    allure.dynamic.title("03 All libraries or processors MUST ensure that the order of the values in the @context property is what is expected for the specific application")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=All%20libraries%20or%20processors%20MUST%20ensure%20that%20the%20order%20of%20the%20values%20in%20the%20%40context%20property%20is%20what%20is%20expected%20for%20the%20specific%20application", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("00 Contexts")
    pytest.skip("TBD")

def test_identifiers_0():
    allure.dynamic.title("00 The id property MUST express an identifier that others are expected to use when expressing statements about a specific thing identified by that identifier.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=The%20id%20property%20MUST%20express%20an%20identifier%20that%20others%20are%20expected%20to%20use%20when%20expressing%20statements%20about%20a%20specific%20thing%20identified%20by%20that%20identifier.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("01 Identifiers")
    pytest.skip("TBD")

def test_identifiers_1():
    allure.dynamic.title("01 The id property MUST NOT have more than one value.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=The%20id%20property%20MUST%20NOT%20have%20more%20than%20one%20value.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("01 Identifiers")
    pytest.skip("TBD")

def test_identifiers_2():
    allure.dynamic.title("02 The value of the id property MUST be a URI.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=The%20value%20of%20the%20id%20property%20MUST%20be%20a%20URI.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("01 Identifiers")
    pytest.skip("TBD")

def test_identifiers_3():
    allure.dynamic.title("03 The value of the id property MUST be a single URI")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=The%20value%20of%20the%20id%20property%20MUST%20be%20a%20single%20URI", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("01 Identifiers")
    pytest.skip("TBD")

def test_types_0():
    allure.dynamic.title("00 Verifiable credentials and verifiable presentations MUST have a type property")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=Verifiable%20credentials%20and%20verifiable%20presentations%20MUST%20have%20a%20type%20property", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("02 Types")
    pytest.skip("TBD")

def test_types_1():
    allure.dynamic.title("01 The value of the type property MUST be, or map to (through interpretation of the @context property), one or more URIs")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=The%20value%20of%20the%20type%20property%20MUST%20be%2C%20or%20map%20to%20%28through%20interpretation%20of%20the%20%40context%20property%29%2C%20one%20or%20more%20URIs", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("02 Types")
    pytest.skip("TBD")

def test_types_2():
    allure.dynamic.title("02 If more than one URI is provided, the URIs MUST be interpreted as an unordered set")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=If%20more%20than%20one%20URI%20is%20provided%2C%20the%20URIs%20MUST%20be%20interpreted%20as%20an%20unordered%20set", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("02 Types")
    pytest.skip("TBD")

def test_types_3():
    allure.dynamic.title("03 With respect to this specification, the following table lists the objects that MUST have a type specified.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=With%20respect%20to%20this%20specification%2C%20the%20following%20table%20lists%20the%20objects%20that%20MUST%20have%20a%20type%20specified.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("02 Types")
    pytest.skip("TBD")

def test_types_4():
    allure.dynamic.title("04 All credentials, presentations, and encapsulated objects MUST specify, or be associated with, additional more narrow types (like UniversityDegreeCredential, for example) so software systems can process this additional information.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=All%20credentials%2C%20presentations%2C%20and%20encapsulated%20objects%20MUST%20specify%2C%20or%20be%20associated%20with%2C%20additional%20more%20narrow%20types%20%28like%20UniversityDegreeCredential%2C%20for%20example%29%20so%20software%20systems%20can%20process%20this%20additional%20information.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("02 Types")
    pytest.skip("TBD")

def test_credential_subject_0():
    allure.dynamic.title("00 A verifiable credential MUST have a credentialSubject property.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=A%20verifiable%20credential%20MUST%20have%20a%20credentialSubject%20property.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("03 Credential subject")
    pytest.skip("TBD")

def test_issuer_0():
    allure.dynamic.title("00 A verifiable credential MUST have an issuer property.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=A%20verifiable%20credential%20MUST%20have%20an%20issuer%20property.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("04 Issuer")
    pytest.skip("TBD")

def test_issuer_1():
    allure.dynamic.title("01 The value of the issuer property MUST be either a URI or an object containing an id property")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=The%20value%20of%20the%20issuer%20property%20MUST%20be%20either%20a%20URI%20or%20an%20object%20containing%20an%20id%20property", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("04 Issuer")
    pytest.skip("TBD")

def test_issuance_date_0():
    allure.dynamic.title("00 A credential MUST have an issuanceDate property")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=A%20credential%20MUST%20have%20an%20issuanceDate%20property", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("05 Issuance date")
    pytest.skip("TBD")

def test_issuance_date_1():
    allure.dynamic.title("01 The value of the issuanceDate property MUST be a string value of an [XMLSCHEMA11-2] combined date-time string representing the date and time the credential becomes valid, which could be a date and time in the future")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=The%20value%20of%20the%20issuanceDate%20property%20MUST%20be%20a%20string%20value%20of%20an%20%5BXMLSCHEMA11%2D2%5D%20combined%20date%2Dtime%20string%20representing%20the%20date%20and%20time%20the%20credential%20becomes%20valid%2C%20which%20could%20be%20a%20date%20and%20time%20in%20the%20future", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("05 Issuance date")
    pytest.skip("TBD")

def test_proofs_signatures_0():
    allure.dynamic.title("00 At least one proof mechanism, and the details necessary to evaluate that proof, MUST be expressed for a credential or presentation to be a verifiable credential or verifiable presentation; that is, to be verifiable.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=At%20least%20one%20proof%20mechanism%2C%20and%20the%20details%20necessary%20to%20evaluate%20that%20proof%2C%20MUST%20be%20expressed%20for%20a%20credential%20or%20presentation%20to%20be%20a%20verifiable%20credential%20or%20verifiable%20presentation%3B%20that%20is%2C%20to%20be%20verifiable.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("06 Proofs signatures")
    pytest.skip("TBD")

def test_proofs_signatures_1():
    allure.dynamic.title("01 When embedding a proof, the proof property MUST be used.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=When%20embedding%20a%20proof%2C%20the%20proof%20property%20MUST%20be%20used.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("06 Proofs signatures")
    pytest.skip("TBD")

def test_proofs_signatures_2():
    allure.dynamic.title("02 The specific method used for an embedded proof MUST be included using the type property.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=The%20specific%20method%20used%20for%20an%20embedded%20proof%20MUST%20be%20included%20using%20the%20type%20property.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("06 Proofs signatures")
    pytest.skip("TBD")

def test_expiration_0():
    allure.dynamic.title("00 If present, the value of the expirationDate property MUST be a string value of an [XMLSCHEMA11-2] date-time representing the date and time the credential ceases to be valid.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=If%20present%2C%20the%20value%20of%20the%20expirationDate%20property%20MUST%20be%20a%20string%20value%20of%20an%20%5BXMLSCHEMA11%2D2%5D%20date%2Dtime%20representing%20the%20date%20and%20time%20the%20credential%20ceases%20to%20be%20valid.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("07 Expiration")
    pytest.skip("TBD")

def test_status_0():
    allure.dynamic.title("00 If present, the value of the credentialStatus property MUST include the following: id property, which MUST be a URI")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=If%20present%2C%20the%20value%20of%20the%20credentialStatus%20property%20MUST%20include%20the%20following%3A%20id%20property%2C%20which%20MUST%20be%20a%20URI", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("08 Status")
    pytest.skip("TBD")

def test_status_1():
    allure.dynamic.title("01 id property, which MUST be a URI.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=id%20property%2C%20which%20MUST%20be%20a%20URI.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("08 Status")
    pytest.skip("TBD")

def test_presentations_0_0():
    allure.dynamic.title("00 If present, the value of the verifiableCredential property MUST be constructed from one or more verifiable credentials, or of data derived from verifiable credentials in a cryptographically verifiable format.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=If%20present%2C%20the%20value%20of%20the%20verifiableCredential%20property%20MUST%20be%20constructed%20from%20one%20or%20more%20verifiable%20credentials%2C%20or%20of%20data%20derived%20from%20verifiable%20credentials%20in%20a%20cryptographically%20verifiable%20format.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("09 Presentations 0")
    pytest.skip("TBD")

def test_extensibility_0():
    allure.dynamic.title("00 JSON-based processors MUST process the @context key, ensuring the expected values exist in the expected order for the credential type being processed")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=JSON%2Dbased%20processors%20MUST%20process%20the%20%40context%20key%2C%20ensuring%20the%20expected%20values%20exist%20in%20the%20expected%20order%20for%20the%20credential%20type%20being%20processed", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("02 Advanced concepts")
    allure.dynamic.sub_suite("00 Extensibility")
    pytest.skip("TBD")

def test_extensibility_1():
    allure.dynamic.title("01 JSON-LD-based processors MUST produce an error when a JSON-LD context redefines any term in the active context")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=JSON%2DLD%2Dbased%20processors%20MUST%20produce%20an%20error%20when%20a%20JSON%2DLD%20context%20redefines%20any%20term%20in%20the%20active%20context", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("02 Advanced concepts")
    allure.dynamic.sub_suite("00 Extensibility")
    pytest.skip("TBD")

def test_data_schemas_0():
    allure.dynamic.title("00 The value of the credentialSchema property MUST be one or more data schemas that provide verifiers with enough information to determine if the provided data conforms to the provided schema")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=The%20value%20of%20the%20credentialSchema%20property%20MUST%20be%20one%20or%20more%20data%20schemas%20that%20provide%20verifiers%20with%20enough%20information%20to%20determine%20if%20the%20provided%20data%20conforms%20to%20the%20provided%20schema", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("02 Advanced concepts")
    allure.dynamic.sub_suite("01 Data schemas")
    pytest.skip("TBD")

def test_data_schemas_1():
    allure.dynamic.title("01 Each credentialSchema MUST specify its type (for example, JsonSchemaValidator2018), and an id property that MUST be a URI identifying the schema file")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=Each%20credentialSchema%20MUST%20specify%20its%20type%20%28for%20example%2C%20JsonSchemaValidator2018%29%2C%20and%20an%20id%20property%20that%20MUST%20be%20a%20URI%20identifying%20the%20schema%20file", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("02 Advanced concepts")
    allure.dynamic.sub_suite("01 Data schemas")
    pytest.skip("TBD")

def test_refreshing_0():
    allure.dynamic.title("00 The value of the refreshService property MUST be one or more refresh services that provides enough information to the recipient's software such that the recipient can refresh the verifiable credential")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=The%20value%20of%20the%20refreshService%20property%20MUST%20be%20one%20or%20more%20refresh%20services%20that%20provides%20enough%20information%20to%20the%20recipient%27s%20software%20such%20that%20the%20recipient%20can%20refresh%20the%20verifiable%20credential", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("02 Advanced concepts")
    allure.dynamic.sub_suite("02 Refreshing")
    pytest.skip("TBD")

def test_refreshing_1():
    allure.dynamic.title("01 Each refreshService value MUST specify its type (for example, ManualRefreshService2018) and its id, which is the URI of the service")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=Each%20refreshService%20value%20MUST%20specify%20its%20type%20%28for%20example%2C%20ManualRefreshService2018%29%20and%20its%20id%2C%20which%20is%20the%20URI%20of%20the%20service", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("02 Advanced concepts")
    allure.dynamic.sub_suite("02 Refreshing")
    pytest.skip("TBD")

def test_terms_of_use_0():
    allure.dynamic.title("00 The value of the termsOfUse property MUST specify one or more terms of use policies under which the creator issued the credential or presentation")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=The%20value%20of%20the%20termsOfUse%20property%20MUST%20specify%20one%20or%20more%20terms%20of%20use%20policies%20under%20which%20the%20creator%20issued%20the%20credential%20or%20presentation", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("02 Advanced concepts")
    allure.dynamic.sub_suite("03 Terms of use")
    pytest.skip("TBD")

def test_terms_of_use_1():
    allure.dynamic.title("01 Each termsOfUse value MUST specify its type, for example, IssuerPolicy, and MAY specify its instance id")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=Each%20termsOfUse%20value%20MUST%20specify%20its%20type%2C%20for%20example%2C%20IssuerPolicy%2C%20and%20MAY%20specify%20its%20instance%20id", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("02 Advanced concepts")
    allure.dynamic.sub_suite("03 Terms of use")
    pytest.skip("TBD")

def test_evidence_0():
    allure.dynamic.title("00 The value of the evidence property MUST be one or more evidence schemes providing enough information for a verifier to determine whether the evidence gathered by the issuer meets its confidence requirements for relying on the credential")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=The%20value%20of%20the%20evidence%20property%20MUST%20be%20one%20or%20more%20evidence%20schemes%20providing%20enough%20information%20for%20a%20verifier%20to%20determine%20whether%20the%20evidence%20gathered%20by%20the%20issuer%20meets%20its%20confidence%20requirements%20for%20relying%20on%20the%20credential", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("02 Advanced concepts")
    allure.dynamic.sub_suite("04 Evidence")
    pytest.skip("TBD")

def test_zero_knowledge_proofs_0():
    allure.dynamic.title("00 The verifiable credential MUST contain a Proof, using the proof property, so that the holder can derive a verifiable presentation that reveals only the information than the holder intends to reveal.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=The%20verifiable%20credential%20MUST%20contain%20a%20Proof%2C%20using%20the%20proof%20property%2C%20so%20that%20the%20holder%20can%20derive%20a%20verifiable%20presentation%20that%20reveals%20only%20the%20information%20than%20the%20holder%20intends%20to%20reveal.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("02 Advanced concepts")
    allure.dynamic.sub_suite("05 Zero knowledge proofs")
    pytest.skip("TBD")

def test_zero_knowledge_proofs_1():
    allure.dynamic.title("01 If a credential definition is being used, the credential definition MUST be defined in the credentialSchema property, so that it can be used by all parties to perform various cryptographic operations in zero-knowledge.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=If%20a%20credential%20definition%20is%20being%20used%2C%20the%20credential%20definition%20MUST%20be%20defined%20in%20the%20credentialSchema%20property%2C%20so%20that%20it%20can%20be%20used%20by%20all%20parties%20to%20perform%20various%20cryptographic%20operations%20in%20zero%2Dknowledge.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("02 Advanced concepts")
    allure.dynamic.sub_suite("05 Zero knowledge proofs")
    pytest.skip("TBD")

def test_zero_knowledge_proofs_2():
    allure.dynamic.title("02 Each derived verifiable credential within a verifiable presentation MUST contain all information necessary to verify the verifiable credential, either by including it directly within the credential, or by referencing the necessary information.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=Each%20derived%20verifiable%20credential%20within%20a%20verifiable%20presentation%20MUST%20contain%20all%20information%20necessary%20to%20verify%20the%20verifiable%20credential%2C%20either%20by%20including%20it%20directly%20within%20the%20credential%2C%20or%20by%20referencing%20the%20necessary%20information.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("02 Advanced concepts")
    allure.dynamic.sub_suite("05 Zero knowledge proofs")
    pytest.skip("TBD")

def test_zero_knowledge_proofs_3():
    allure.dynamic.title("03 A verifiable presentation MUST NOT leak information that would enable the verifier to correlate the holder across multiple verifiable presentations.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=A%20verifiable%20presentation%20MUST%20NOT%20leak%20information%20that%20would%20enable%20the%20verifier%20to%20correlate%20the%20holder%20across%20multiple%20verifiable%20presentations.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("02 Advanced concepts")
    allure.dynamic.sub_suite("05 Zero knowledge proofs")
    pytest.skip("TBD")

def test_json_0():
    allure.dynamic.title("00 Other values MUST be represented as a String type.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=Other%20values%20MUST%20be%20represented%20as%20a%20String%20type.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("03 Syntaxes")
    allure.dynamic.sub_suite("00 Json")
    pytest.skip("TBD")

def test_proof_formats_0():
    allure.dynamic.title("00 vc: JSON object, which MUST be present in a JWT verifiable credential")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=vc%3A%20JSON%20object%2C%20which%20MUST%20be%20present%20in%20a%20JWT%20verifiable%20credential", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("03 Syntaxes")
    allure.dynamic.sub_suite("01 Proof formats")
    pytest.skip("TBD")

def test_proof_formats_1():
    allure.dynamic.title("01 vp: JSON object, which MUST be present in a JWT verifiable presentation")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=vp%3A%20JSON%20object%2C%20which%20MUST%20be%20present%20in%20a%20JWT%20verifiable%20presentation", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("03 Syntaxes")
    allure.dynamic.sub_suite("01 Proof formats")
    pytest.skip("TBD")

def test_proof_formats_2():
    allure.dynamic.title("02 To encode a verifiable credential as a JWT, specific properties introduced by this specification MUST be either:")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=To%20encode%20a%20verifiable%20credential%20as%20a%20JWT%2C%20specific%20properties%20introduced%20by%20this%20specification%20MUST%20be%20either%3A", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("03 Syntaxes")
    allure.dynamic.sub_suite("01 Proof formats")
    pytest.skip("TBD")

def test_proof_formats_3():
    allure.dynamic.title("03 If no JWS is present, a proof property MUST be provided")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=If%20no%20JWS%20is%20present%2C%20a%20proof%20property%20MUST%20be%20provided", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("03 Syntaxes")
    allure.dynamic.sub_suite("01 Proof formats")
    pytest.skip("TBD")

def test_proof_formats_4():
    allure.dynamic.title("04 For backward compatibility reasons, the issuer MUST use JWS to represent proofs based on a digital signature.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=For%20backward%20compatibility%20reasons%2C%20the%20issuer%20MUST%20use%20JWS%20to%20represent%20proofs%20based%20on%20a%20digital%20signature.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("03 Syntaxes")
    allure.dynamic.sub_suite("01 Proof formats")
    pytest.skip("TBD")

def test_proof_formats_5():
    allure.dynamic.title("05 alg MUST be set for digital signatures")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=alg%20MUST%20be%20set%20for%20digital%20signatures", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("03 Syntaxes")
    allure.dynamic.sub_suite("01 Proof formats")
    pytest.skip("TBD")

def test_proof_formats_6():
    allure.dynamic.title("06 If only the proof property is needed for the chosen signature method (that is, if there is no choice of algorithm within that method), the alg header MUST be set to none.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=If%20only%20the%20proof%20property%20is%20needed%20for%20the%20chosen%20signature%20method%20%28that%20is%2C%20if%20there%20is%20no%20choice%20of%20algorithm%20within%20that%20method%29%2C%20the%20alg%20header%20MUST%20be%20set%20to%20none.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("03 Syntaxes")
    allure.dynamic.sub_suite("01 Proof formats")
    pytest.skip("TBD")

def test_proof_formats_7():
    allure.dynamic.title("07 typ, if present, MUST be set to JWT.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=typ%2C%20if%20present%2C%20MUST%20be%20set%20to%20JWT.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("03 Syntaxes")
    allure.dynamic.sub_suite("01 Proof formats")
    pytest.skip("TBD")

def test_proof_formats_8():
    allure.dynamic.title("08 For backward compatibility with JWT processors, the following registered JWT claim names MUST be used, instead of or in addition to, their respective standard verifiable credential counterparts:")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=For%20backward%20compatibility%20with%20JWT%20processors%2C%20the%20following%20registered%20JWT%20claim%20names%20MUST%20be%20used%2C%20instead%20of%20or%20in%20addition%20to%2C%20their%20respective%20standard%20verifiable%20credential%20counterparts%3A", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("03 Syntaxes")
    allure.dynamic.sub_suite("01 Proof formats")
    pytest.skip("TBD")

def test_proof_formats_9():
    allure.dynamic.title("09 exp MUST represent the expirationDate property, encoded as a UNIX timestamp (NumericDate).")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=exp%20MUST%20represent%20the%20expirationDate%20property%2C%20encoded%20as%20a%20UNIX%20timestamp%20%28NumericDate%29.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("03 Syntaxes")
    allure.dynamic.sub_suite("01 Proof formats")
    pytest.skip("TBD")

def test_proof_formats_10():
    allure.dynamic.title("10 iss MUST represent the issuer property of a verifiable credential or the holder property of a verifiable presentation.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=iss%20MUST%20represent%20the%20issuer%20property%20of%20a%20verifiable%20credential%20or%20the%20holder%20property%20of%20a%20verifiable%20presentation.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("03 Syntaxes")
    allure.dynamic.sub_suite("01 Proof formats")
    pytest.skip("TBD")

def test_proof_formats_11():
    allure.dynamic.title("11 nbf MUST represent issuanceDate, encoded as a UNIX timestamp (NumericDate).")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=nbf%20MUST%20represent%20issuanceDate%2C%20encoded%20as%20a%20UNIX%20timestamp%20%28NumericDate%29.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("03 Syntaxes")
    allure.dynamic.sub_suite("01 Proof formats")
    pytest.skip("TBD")

def test_proof_formats_12():
    allure.dynamic.title("12 jti MUST represent the id property of the verifiable credential or verifiable presentation.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=jti%20MUST%20represent%20the%20id%20property%20of%20the%20verifiable%20credential%20or%20verifiable%20presentation.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("03 Syntaxes")
    allure.dynamic.sub_suite("01 Proof formats")
    pytest.skip("TBD")

def test_proof_formats_13():
    allure.dynamic.title("13 sub MUST represent the id property contained in the credentialSubject")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=sub%20MUST%20represent%20the%20id%20property%20contained%20in%20the%20credentialSubject", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("03 Syntaxes")
    allure.dynamic.sub_suite("01 Proof formats")
    pytest.skip("TBD")

def test_proof_formats_14():
    allure.dynamic.title("14 aud MUST represent (i.e., identify) the intended audience of the verifiable presentation (i.e., the verifier intended by the presenting holder to receive and verify the verifiable presentation).")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=aud%20MUST%20represent%20%28i.e.%2C%20identify%29%20the%20intended%20audience%20of%20the%20verifiable%20presentation%20%28i.e.%2C%20the%20verifier%20intended%20by%20the%20presenting%20holder%20to%20receive%20and%20verify%20the%20verifiable%20presentation%29.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("03 Syntaxes")
    allure.dynamic.sub_suite("01 Proof formats")
    pytest.skip("TBD")

def test_proof_formats_15():
    allure.dynamic.title("15 Additional verifiable credential claims MUST be added to the credentialSubject property of the JWT.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=Additional%20verifiable%20credential%20claims%20MUST%20be%20added%20to%20the%20credentialSubject%20property%20of%20the%20JWT.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("03 Syntaxes")
    allure.dynamic.sub_suite("01 Proof formats")
    pytest.skip("TBD")

def test_proof_formats_16():
    allure.dynamic.title("16 To decode a JWT to a standard credential or presentation, the following transformation MUST be performed:")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=To%20decode%20a%20JWT%20to%20a%20standard%20credential%20or%20presentation%2C%20the%20following%20transformation%20MUST%20be%20performed%3A", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("03 Syntaxes")
    allure.dynamic.sub_suite("01 Proof formats")
    pytest.skip("TBD")

def test_proof_formats_17():
    allure.dynamic.title("17 To transform the JWT specific headers and claims, the following MUST be done:")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=To%20transform%20the%20JWT%20specific%20headers%20and%20claims%2C%20the%20following%20MUST%20be%20done%3A", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("03 Syntaxes")
    allure.dynamic.sub_suite("01 Proof formats")
    pytest.skip("TBD")

def test_proof_formats_18():
    allure.dynamic.title("18 If exp is present, the UNIX timestamp MUST be converted to an [XMLSCHEMA11-2] date-time, and MUST be used to set the value of the expirationDate property of credentialSubject of the new JSON object.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=If%20exp%20is%20present%2C%20the%20UNIX%20timestamp%20MUST%20be%20converted%20to%20an%20%5BXMLSCHEMA11%2D2%5D%20date%2Dtime%2C%20and%20MUST%20be%20used%20to%20set%20the%20value%20of%20the%20expirationDate%20property%20of%20credentialSubject%20of%20the%20new%20JSON%20object.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("03 Syntaxes")
    allure.dynamic.sub_suite("01 Proof formats")
    pytest.skip("TBD")

def test_proof_formats_19():
    allure.dynamic.title("19 If iss is present, the value MUST be used to set the issuer property of the new credential JSON object or the holder property of the new presentation JSON object.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=If%20iss%20is%20present%2C%20the%20value%20MUST%20be%20used%20to%20set%20the%20issuer%20property%20of%20the%20new%20credential%20JSON%20object%20or%20the%20holder%20property%20of%20the%20new%20presentation%20JSON%20object.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("03 Syntaxes")
    allure.dynamic.sub_suite("01 Proof formats")
    pytest.skip("TBD")

def test_proof_formats_20():
    allure.dynamic.title("20 If nbf is present, the UNIX timestamp MUST be converted to an [XMLSCHEMA11-2] date-time, and MUST be used to set the value of the issuanceDate property of the new JSON object.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=If%20nbf%20is%20present%2C%20the%20UNIX%20timestamp%20MUST%20be%20converted%20to%20an%20%5BXMLSCHEMA11%2D2%5D%20date%2Dtime%2C%20and%20MUST%20be%20used%20to%20set%20the%20value%20of%20the%20issuanceDate%20property%20of%20the%20new%20JSON%20object.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("03 Syntaxes")
    allure.dynamic.sub_suite("01 Proof formats")
    pytest.skip("TBD")

def test_proof_formats_21():
    allure.dynamic.title("21 If sub is present, the value MUST be used to set the value of the id property of credentialSubject of the new credential JSON object.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=If%20sub%20is%20present%2C%20the%20value%20MUST%20be%20used%20to%20set%20the%20value%20of%20the%20id%20property%20of%20credentialSubject%20of%20the%20new%20credential%20JSON%20object.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("03 Syntaxes")
    allure.dynamic.sub_suite("01 Proof formats")
    pytest.skip("TBD")

def test_proof_formats_22():
    allure.dynamic.title("22 If jti is present, the value MUST be used to set the value of the id property of the new JSON object.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model/#:~:text=If%20jti%20is%20present%2C%20the%20value%20MUST%20be%20used%20to%20set%20the%20value%20of%20the%20id%20property%20of%20the%20new%20JSON%20object.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v1.1")
    allure.dynamic.suite("03 Syntaxes")
    allure.dynamic.sub_suite("01 Proof formats")
    pytest.skip("TBD")
