import allure
import pytest

def test_conformance_0():
    allure.dynamic.title("00 The key words MAY, MUST, MUST NOT, OPTIONAL, RECOMMENDED, REQUIRED, SHOULD, and SHOULD NOT in this document are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all capitals, as shown here.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=The%20key%20words%20MAY%2C%20MUST%2C%20MUST%20NOT%2C%20OPTIONAL%2C%20RECOMMENDED%2C%20REQUIRED%2C%20SHOULD%2C%20and%20SHOULD%20NOT%20in%20this%20document%20are%20to%20be%20interpreted%20as%20described%20in%20BCP%2014%20%5BRFC2119%5D%20%5BRFC8174%5D%20when%2C%20and%20only%20when%2C%20they%20appear%20in%20all%20capitals%2C%20as%20shown%20here.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("00 Introduction")
    allure.dynamic.sub_suite("00 Conformance")
    pytest.skip("TBD")

def test_conformance_1():
    allure.dynamic.title("01 A conforming document is a compacted JSON-LD document that complies with all of the relevant 'MUST' statements in this specification")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=A%20conforming%20document%20is%20a%20compacted%20JSON%2DLD%20document%20that%20complies%20with%20all%20of%20the%20relevant%20%27MUST%27%20statements%20in%20this%20specification", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("00 Introduction")
    allure.dynamic.sub_suite("00 Conformance")
    pytest.skip("TBD")

def test_conformance_2():
    allure.dynamic.title("02 Specifically, the relevant normative 'MUST' statements in Sections 4")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=Specifically%2C%20the%20relevant%20normative%20%27MUST%27%20statements%20in%20Sections%204", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("00 Introduction")
    allure.dynamic.sub_suite("00 Conformance")
    pytest.skip("TBD")

def test_conformance_3():
    allure.dynamic.title("03 Syntaxes of this document MUST be enforced")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=Syntaxes%20of%20this%20document%20MUST%20be%20enforced", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("00 Introduction")
    allure.dynamic.sub_suite("00 Conformance")
    pytest.skip("TBD")

def test_conformance_4():
    allure.dynamic.title("04 A conforming document MUST be either a verifiable credential with a media type of application/vc or a verifiable presentation with a media type of application/vp")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=A%20conforming%20document%20MUST%20be%20either%20a%20verifiable%20credential%20with%20a%20media%20type%20of%20application/vc%20or%20a%20verifiable%20presentation%20with%20a%20media%20type%20of%20application/vp", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("00 Introduction")
    allure.dynamic.sub_suite("00 Conformance")
    pytest.skip("TBD")

def test_conformance_5():
    allure.dynamic.title("05 A conforming document MUST be secured by at least one securing mechanism as described in Section 4.12 Securing Mechanisms.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=A%20conforming%20document%20MUST%20be%20secured%20by%20at%20least%20one%20securing%20mechanism%20as%20described%20in%20Section%204.12%20Securing%20Mechanisms.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("00 Introduction")
    allure.dynamic.sub_suite("00 Conformance")
    pytest.skip("TBD")

def test_conformance_6():
    allure.dynamic.title("06 A conforming issuer implementation produces conforming documents, MUST include all required properties in the conforming documents it produces, and MUST secure the conforming documents it produces using a securing mechanism described in Section 4.12 Securing Mechanisms.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=A%20conforming%20issuer%20implementation%20produces%20conforming%20documents%2C%20MUST%20include%20all%20required%20properties%20in%20the%20conforming%20documents%20it%20produces%2C%20and%20MUST%20secure%20the%20conforming%20documents%20it%20produces%20using%20a%20securing%20mechanism%20described%20in%20Section%204.12%20Securing%20Mechanisms.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("00 Introduction")
    allure.dynamic.sub_suite("00 Conformance")
    pytest.skip("TBD")

def test_conformance_7():
    allure.dynamic.title("07 A conforming verifier implementation consumes conforming documents, MUST perform verification on a conforming document as described in Section 4.12 Securing Mechanisms, MUST check that each required property satisfies the normative requirements for that property, and MUST produce errors when non-conforming documents are detected.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=A%20conforming%20verifier%20implementation%20consumes%20conforming%20documents%2C%20MUST%20perform%20verification%20on%20a%20conforming%20document%20as%20described%20in%20Section%204.12%20Securing%20Mechanisms%2C%20MUST%20check%20that%20each%20required%20property%20satisfies%20the%20normative%20requirements%20for%20that%20property%2C%20and%20MUST%20produce%20errors%20when%20non%2Dconforming%20documents%20are%20detected.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("00 Introduction")
    allure.dynamic.sub_suite("00 Conformance")
    pytest.skip("TBD")

def test_contexts_0():
    allure.dynamic.title("00 Verifiable credentials and verifiable presentations MUST include a @context property")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=Verifiable%20credentials%20and%20verifiable%20presentations%20MUST%20include%20a%20%40context%20property", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("00 Contexts")
    pytest.skip("TBD")

def test_contexts_1():
    allure.dynamic.title("01 Application developers MUST understand every JSON-LD context used by their application, at least to the extent that it affects the meaning of the terms used by their application")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=Application%20developers%20MUST%20understand%20every%20JSON%2DLD%20context%20used%20by%20their%20application%2C%20at%20least%20to%20the%20extent%20that%20it%20affects%20the%20meaning%20of%20the%20terms%20used%20by%20their%20application", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("00 Contexts")
    pytest.skip("TBD")

def test_contexts_2():
    allure.dynamic.title("02 The value of the @context property MUST be an ordered set where the first item is a URL with the value https://www.w3.org/ns/credentials/v2")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=The%20value%20of%20the%20%40context%20property%20MUST%20be%20an%20ordered%20set%20where%20the%20first%20item%20is%20a%20URL%20with%20the%20value%20https%3A//www.w3.org/ns/credentials/v2", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("00 Contexts")
    pytest.skip("TBD")

def test_contexts_3():
    allure.dynamic.title("03 Subsequent items in the ordered set MUST be composed of any combination of URLs and objects, where each is processable as a JSON-LD Context.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=Subsequent%20items%20in%20the%20ordered%20set%20MUST%20be%20composed%20of%20any%20combination%20of%20URLs%20and%20objects%2C%20where%20each%20is%20processable%20as%20a%20JSON%2DLD%20Context.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("00 Contexts")
    pytest.skip("TBD")

def test_identifiers_0():
    allure.dynamic.title("00 If present, id property's value MUST be a single URL, which MAY be dereferenceable")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=If%20present%2C%20id%20property%27s%20value%20MUST%20be%20a%20single%20URL%2C%20which%20MAY%20be%20dereferenceable", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("01 Identifiers")
    pytest.skip("TBD")

def test_types_0():
    allure.dynamic.title("00 Verifiable credentials and verifiable presentations MUST contain a type property with an associated value.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=Verifiable%20credentials%20and%20verifiable%20presentations%20MUST%20contain%20a%20type%20property%20with%20an%20associated%20value.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("02 Types")
    pytest.skip("TBD")

def test_types_1():
    allure.dynamic.title("01 The value of the type property MUST be one or more terms and absolute URL strings")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=The%20value%20of%20the%20type%20property%20MUST%20be%20one%20or%20more%20terms%20and%20absolute%20URL%20strings", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("02 Types")
    pytest.skip("TBD")

def test_types_2():
    allure.dynamic.title("02 Concerning this specification, the following table lists the objects that MUST have a type specified.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=Concerning%20this%20specification%2C%20the%20following%20table%20lists%20the%20objects%20that%20MUST%20have%20a%20type%20specified.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("02 Types")
    pytest.skip("TBD")

def test_names_and_descriptions_0():
    allure.dynamic.title("00 If present, the value of the name property MUST be a string or a language value object as described in 11.1 Language and Base Direction")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=If%20present%2C%20the%20value%20of%20the%20name%20property%20MUST%20be%20a%20string%20or%20a%20language%20value%20object%20as%20described%20in%2011.1%20Language%20and%20Base%20Direction", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("03 Names and descriptions")
    pytest.skip("TBD")

def test_names_and_descriptions_1():
    allure.dynamic.title("01 If present, the value of the description property MUST be a string or a language value object as described in 11.1 Language and Base Direction")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=If%20present%2C%20the%20value%20of%20the%20description%20property%20MUST%20be%20a%20string%20or%20a%20language%20value%20object%20as%20described%20in%2011.1%20Language%20and%20Base%20Direction", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("03 Names and descriptions")
    pytest.skip("TBD")

def test_issuer_0():
    allure.dynamic.title("00 A verifiable credential MUST have an issuer property.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=A%20verifiable%20credential%20MUST%20have%20an%20issuer%20property.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("04 Issuer")
    pytest.skip("TBD")

def test_issuer_1():
    allure.dynamic.title("01 The value of the issuer property MUST be either a URL or an object containing an id property whose value is a URL; in either case, the issuer selects this URL to identify itself in a globally unambiguous way")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=The%20value%20of%20the%20issuer%20property%20MUST%20be%20either%20a%20URL%20or%20an%20object%20containing%20an%20id%20property%20whose%20value%20is%20a%20URL%3B%20in%20either%20case%2C%20the%20issuer%20selects%20this%20URL%20to%20identify%20itself%20in%20a%20globally%20unambiguous%20way", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("04 Issuer")
    pytest.skip("TBD")

def test_credential_subject_0():
    allure.dynamic.title("00 A verifiable credential MUST contain a credentialSubject property.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=A%20verifiable%20credential%20MUST%20contain%20a%20credentialSubject%20property.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("05 Credential subject")
    pytest.skip("TBD")

def test_credential_subject_1():
    allure.dynamic.title("01 The value of the credentialSubject property is a set of objects where each object MUST be the subject of one or more claims, which MUST be serialized inside the credentialSubject property")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=The%20value%20of%20the%20credentialSubject%20property%20is%20a%20set%20of%20objects%20where%20each%20object%20MUST%20be%20the%20subject%20of%20one%20or%20more%20claims%2C%20which%20MUST%20be%20serialized%20inside%20the%20credentialSubject%20property", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("05 Credential subject")
    pytest.skip("TBD")

def test_validity_period_0():
    allure.dynamic.title("00 If present, the value of the validFrom property MUST be a [XMLSCHEMA11-2] dateTimeStamp string value representing the date and time the credential becomes valid, which could be a date and time in the future or the past")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=If%20present%2C%20the%20value%20of%20the%20validFrom%20property%20MUST%20be%20a%20%5BXMLSCHEMA11%2D2%5D%20dateTimeStamp%20string%20value%20representing%20the%20date%20and%20time%20the%20credential%20becomes%20valid%2C%20which%20could%20be%20a%20date%20and%20time%20in%20the%20future%20or%20the%20past", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("06 Validity period")
    pytest.skip("TBD")

def test_validity_period_1():
    allure.dynamic.title("01 If a validUntil value also exists, the validFrom value MUST express a point in time that is temporally the same or earlier than the point in time expressed by the validUntil value.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=If%20a%20validUntil%20value%20also%20exists%2C%20the%20validFrom%20value%20MUST%20express%20a%20point%20in%20time%20that%20is%20temporally%20the%20same%20or%20earlier%20than%20the%20point%20in%20time%20expressed%20by%20the%20validUntil%20value.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("06 Validity period")
    pytest.skip("TBD")

def test_validity_period_2():
    allure.dynamic.title("02 If present, the value of the validUntil property MUST be a [XMLSCHEMA11-2] dateTimeStamp string value representing the date and time the credential ceases to be valid, which could be a date and time in the past or the future")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=If%20present%2C%20the%20value%20of%20the%20validUntil%20property%20MUST%20be%20a%20%5BXMLSCHEMA11%2D2%5D%20dateTimeStamp%20string%20value%20representing%20the%20date%20and%20time%20the%20credential%20ceases%20to%20be%20valid%2C%20which%20could%20be%20a%20date%20and%20time%20in%20the%20past%20or%20the%20future", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("06 Validity period")
    pytest.skip("TBD")

def test_validity_period_3():
    allure.dynamic.title("03 If a validFrom value also exists, the validUntil value MUST express a point in time that is temporally the same or later than the point in time expressed by the validFrom value.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=If%20a%20validFrom%20value%20also%20exists%2C%20the%20validUntil%20value%20MUST%20express%20a%20point%20in%20time%20that%20is%20temporally%20the%20same%20or%20later%20than%20the%20point%20in%20time%20expressed%20by%20the%20validFrom%20value.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("06 Validity period")
    pytest.skip("TBD")

def test_status_0():
    allure.dynamic.title("00 If present, the normative guidance in Section 4.4 Identifiers MUST be followed.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=If%20present%2C%20the%20normative%20guidance%20in%20Section%204.4%20Identifiers%20MUST%20be%20followed.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("07 Status")
    pytest.skip("TBD")

def test_status_1():
    allure.dynamic.title("01 The type property is REQUIRED")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=The%20type%20property%20is%20REQUIRED", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("07 Status")
    pytest.skip("TBD")

def test_status_2():
    allure.dynamic.title("02 The related normative guidance in Section 4.5 Types MUST be followed.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=The%20related%20normative%20guidance%20in%20Section%204.5%20Types%20MUST%20be%20followed.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("07 Status")
    pytest.skip("TBD")

def test_status_3():
    allure.dynamic.title("03 Credential status specifications MUST NOT enable tracking of individuals, such as an issuer being notified (either directly or indirectly) when a verifier is interested in a specific holder or subject")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=Credential%20status%20specifications%20MUST%20NOT%20enable%20tracking%20of%20individuals%2C%20such%20as%20an%20issuer%20being%20notified%20%28either%20directly%20or%20indirectly%29%20when%20a%20verifier%20is%20interested%20in%20a%20specific%20holder%20or%20subject", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("07 Status")
    pytest.skip("TBD")

def test_data_schemas_0():
    allure.dynamic.title("00 The value of the credentialSchema property MUST be one or more data schemas that provide verifiers with enough information to determine whether the provided data conforms to the provided schema(s)")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=The%20value%20of%20the%20credentialSchema%20property%20MUST%20be%20one%20or%20more%20data%20schemas%20that%20provide%20verifiers%20with%20enough%20information%20to%20determine%20whether%20the%20provided%20data%20conforms%20to%20the%20provided%20schema%28s%29", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("08 Data schemas")
    pytest.skip("TBD")

def test_data_schemas_1():
    allure.dynamic.title("01 Each credentialSchema MUST specify its type (for example, JsonSchema) and an id property that MUST be a URL identifying the schema file")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=Each%20credentialSchema%20MUST%20specify%20its%20type%20%28for%20example%2C%20JsonSchema%29%20and%20an%20id%20property%20that%20MUST%20be%20a%20URL%20identifying%20the%20schema%20file", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("08 Data schemas")
    pytest.skip("TBD")

def test_verifiable_presentations_0():
    allure.dynamic.title("00 If present, the normative guidance in Section 4.4 Identifiers MUST be followed.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=If%20present%2C%20the%20normative%20guidance%20in%20Section%204.4%20Identifiers%20MUST%20be%20followed.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("09 Verifiable presentations")
    pytest.skip("TBD")

def test_verifiable_presentations_1():
    allure.dynamic.title("01 The type property MUST be present")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=The%20type%20property%20MUST%20be%20present", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("09 Verifiable presentations")
    pytest.skip("TBD")

def test_verifiable_presentations_2():
    allure.dynamic.title("02 One value of this property MUST be VerifiablePresentation, but additional types MAY be included")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=One%20value%20of%20this%20property%20MUST%20be%20VerifiablePresentation%2C%20but%20additional%20types%20MAY%20be%20included", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("09 Verifiable presentations")
    pytest.skip("TBD")

def test_verifiable_presentations_3():
    allure.dynamic.title("03 The related normative guidance in Section 4.5 Types MUST be followed.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=The%20related%20normative%20guidance%20in%20Section%204.5%20Types%20MUST%20be%20followed.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("09 Verifiable presentations")
    pytest.skip("TBD")

def test_verifiable_presentations_4():
    allure.dynamic.title("04 The value MUST be one or more verifiable credential and/or enveloped verifiable credential objects (the values MUST NOT be non-object values such as numbers, strings, or URLs)")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=The%20value%20MUST%20be%20one%20or%20more%20verifiable%20credential%20and/or%20enveloped%20verifiable%20credential%20objects%20%28the%20values%20MUST%20NOT%20be%20non%2Dobject%20values%20such%20as%20numbers%2C%20strings%2C%20or%20URLs%29", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("09 Verifiable presentations")
    pytest.skip("TBD")

def test_verifiable_presentations_5():
    allure.dynamic.title("05 These objects are called verifiable credential graphs and MUST express information that is secured using a securing mechanism")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=These%20objects%20are%20called%20verifiable%20credential%20graphs%20and%20MUST%20express%20information%20that%20is%20secured%20using%20a%20securing%20mechanism", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("09 Verifiable presentations")
    pytest.skip("TBD")

def test_verifiable_presentations_6():
    allure.dynamic.title("06 If present, the value MUST be either a URL or an object containing an id property")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=If%20present%2C%20the%20value%20MUST%20be%20either%20a%20URL%20or%20an%20object%20containing%20an%20id%20property", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("09 Verifiable presentations")
    pytest.skip("TBD")

def test_verifiable_presentations_7():
    allure.dynamic.title("07 The @context property of the object MUST be present and include a context, such as the base context for this specification, that defines at least the id, type, and EnvelopedVerifiableCredential terms as defined by the base context provided by this specification")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=The%20%40context%20property%20of%20the%20object%20MUST%20be%20present%20and%20include%20a%20context%2C%20such%20as%20the%20base%20context%20for%20this%20specification%2C%20that%20defines%20at%20least%20the%20id%2C%20type%2C%20and%20EnvelopedVerifiableCredential%20terms%20as%20defined%20by%20the%20base%20context%20provided%20by%20this%20specification", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("09 Verifiable presentations")
    pytest.skip("TBD")

def test_verifiable_presentations_8():
    allure.dynamic.title("08 The id value of the object MUST be a data: URL [RFC2397] that expresses a secured verifiable credential using an enveloping security scheme, such as Securing Verifiable Credentials using JOSE and COSE [VC-JOSE-COSE]")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=The%20id%20value%20of%20the%20object%20MUST%20be%20a%20data%3A%20URL%20%5BRFC2397%5D%20that%20expresses%20a%20secured%20verifiable%20credential%20using%20an%20enveloping%20security%20scheme%2C%20such%20as%20Securing%20Verifiable%20Credentials%20using%20JOSE%20and%20COSE%20%5BVC%2DJOSE%2DCOSE%5D", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("09 Verifiable presentations")
    pytest.skip("TBD")

def test_verifiable_presentations_9():
    allure.dynamic.title("09 The type value of the object MUST be EnvelopedVerifiableCredential.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=The%20type%20value%20of%20the%20object%20MUST%20be%20EnvelopedVerifiableCredential.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("09 Verifiable presentations")
    pytest.skip("TBD")

def test_verifiable_presentations_10():
    allure.dynamic.title("10 The @context property of the object MUST be present and include a context, such as the base context for this specification, that defines at least the id, type, and EnvelopedVerifiablePresentation terms as defined by the base context provided by this specification")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=The%20%40context%20property%20of%20the%20object%20MUST%20be%20present%20and%20include%20a%20context%2C%20such%20as%20the%20base%20context%20for%20this%20specification%2C%20that%20defines%20at%20least%20the%20id%2C%20type%2C%20and%20EnvelopedVerifiablePresentation%20terms%20as%20defined%20by%20the%20base%20context%20provided%20by%20this%20specification", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("09 Verifiable presentations")
    pytest.skip("TBD")

def test_verifiable_presentations_11():
    allure.dynamic.title("11 The id value of the object MUST be a data: URL [RFC2397] that expresses a secured verifiable presentation using an enveloping securing mechanism, such as Securing Verifiable Credentials using JOSE and COSE [VC-JOSE-COSE]")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=The%20id%20value%20of%20the%20object%20MUST%20be%20a%20data%3A%20URL%20%5BRFC2397%5D%20that%20expresses%20a%20secured%20verifiable%20presentation%20using%20an%20enveloping%20securing%20mechanism%2C%20such%20as%20Securing%20Verifiable%20Credentials%20using%20JOSE%20and%20COSE%20%5BVC%2DJOSE%2DCOSE%5D", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("09 Verifiable presentations")
    pytest.skip("TBD")

def test_verifiable_presentations_12():
    allure.dynamic.title("12 The type value of the object MUST be EnvelopedVerifiablePresentation.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=The%20type%20value%20of%20the%20object%20MUST%20be%20EnvelopedVerifiablePresentation.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("09 Verifiable presentations")
    pytest.skip("TBD")

def test_verifiable_presentations_13():
    allure.dynamic.title("13 A verifiable presentation that includes a self-asserted verifiable credential, which is secured only using the same mechanism as the verifiable presentation, MUST include a holder property.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=A%20verifiable%20presentation%20that%20includes%20a%20self%2Dasserted%20verifiable%20credential%2C%20which%20is%20secured%20only%20using%20the%20same%20mechanism%20as%20the%20verifiable%20presentation%2C%20MUST%20include%20a%20holder%20property.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("09 Verifiable presentations")
    pytest.skip("TBD")

def test_verifiable_presentations_14():
    allure.dynamic.title("14 When a self-asserted verifiable credential is secured using the same mechanism as the verifiable presentation, the value of the issuer property of the verifiable credential MUST be identical to the holder property of the verifiable presentation.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=When%20a%20self%2Dasserted%20verifiable%20credential%20is%20secured%20using%20the%20same%20mechanism%20as%20the%20verifiable%20presentation%2C%20the%20value%20of%20the%20issuer%20property%20of%20the%20verifiable%20credential%20MUST%20be%20identical%20to%20the%20holder%20property%20of%20the%20verifiable%20presentation.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("01 Basic concepts")
    allure.dynamic.sub_suite("09 Verifiable presentations")
    pytest.skip("TBD")

def test_extensibility_0():
    allure.dynamic.title("00 New terms MUST define a new URL for each term")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=New%20terms%20MUST%20define%20a%20new%20URL%20for%20each%20term", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("02 Advanced concepts")
    allure.dynamic.sub_suite("00 Extensibility")
    pytest.skip("TBD")

def test_extensibility_1():
    allure.dynamic.title("01 When doing so, the general guidelines for [LINKED-DATA] are expected to be followed, in particular: Human-readable documentation MUST be published, describing the semantics of and the constraints on the use of each term")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=When%20doing%20so%2C%20the%20general%20guidelines%20for%20%5BLINKED%2DDATA%5D%20are%20expected%20to%20be%20followed%2C%20in%20particular%3A%20Human%2Dreadable%20documentation%20MUST%20be%20published%2C%20describing%20the%20semantics%20of%20and%20the%20constraints%20on%20the%20use%20of%20each%20term", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("02 Advanced concepts")
    allure.dynamic.sub_suite("00 Extensibility")
    pytest.skip("TBD")

def test_extensibility_2():
    allure.dynamic.title("02 Human-readable documentation MUST be published, describing the semantics of and the constraints on the use of each term.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=Human%2Dreadable%20documentation%20MUST%20be%20published%2C%20describing%20the%20semantics%20of%20and%20the%20constraints%20on%20the%20use%20of%20each%20term.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("02 Advanced concepts")
    allure.dynamic.sub_suite("00 Extensibility")
    pytest.skip("TBD")

def test_extensibility_3():
    allure.dynamic.title("03 Furthermore, a machine-readable description (that is, a JSON-LD Context document) MUST be published at the URL specified in the @context property for the vocabulary")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=Furthermore%2C%20a%20machine%2Dreadable%20description%20%28that%20is%2C%20a%20JSON%2DLD%20Context%20document%29%20MUST%20be%20published%20at%20the%20URL%20specified%20in%20the%20%40context%20property%20for%20the%20vocabulary", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("02 Advanced concepts")
    allure.dynamic.sub_suite("00 Extensibility")
    pytest.skip("TBD")

def test_extensibility_4():
    allure.dynamic.title("04 This context MUST map each term to its corresponding URL, possibly accompanied by further constraints like the type of the property value")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=This%20context%20MUST%20map%20each%20term%20to%20its%20corresponding%20URL%2C%20possibly%20accompanied%20by%20further%20constraints%20like%20the%20type%20of%20the%20property%20value", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("02 Advanced concepts")
    allure.dynamic.sub_suite("00 Extensibility")
    pytest.skip("TBD")

def test_extensibility_5():
    allure.dynamic.title("05 If a conforming document does not use JSON-LD Contexts that define all terms used, it MUST include the https://www.w3.org/ns/credentials/undefined-terms/v2 as the last value in the @context property.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=If%20a%20conforming%20document%20does%20not%20use%20JSON%2DLD%20Contexts%20that%20define%20all%20terms%20used%2C%20it%20MUST%20include%20the%20https%3A//www.w3.org/ns/credentials/undefined%2Dterms/v2%20as%20the%20last%20value%20in%20the%20%40context%20property.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("02 Advanced concepts")
    allure.dynamic.sub_suite("00 Extensibility")
    pytest.skip("TBD")

def test_integrity_of_related_resources_0():
    allure.dynamic.title("00 The value of the relatedResource property MUST be one or more objects of the following form: Property Description id The identifier for the resource is REQUIRED and conforms to the format defined in Section 4.4 Identifiers")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=The%20value%20of%20the%20relatedResource%20property%20MUST%20be%20one%20or%20more%20objects%20of%20the%20following%20form%3A%20Property%20Description%20id%20The%20identifier%20for%20the%20resource%20is%20REQUIRED%20and%20conforms%20to%20the%20format%20defined%20in%20Section%204.4%20Identifiers", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("02 Advanced concepts")
    allure.dynamic.sub_suite("01 Integrity of related resources")
    pytest.skip("TBD")

def test_integrity_of_related_resources_1():
    allure.dynamic.title("01 The value MUST be unique among the list of related resource objects")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=The%20value%20MUST%20be%20unique%20among%20the%20list%20of%20related%20resource%20objects", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("02 Advanced concepts")
    allure.dynamic.sub_suite("01 Integrity of related resources")
    pytest.skip("TBD")

def test_integrity_of_related_resources_2():
    allure.dynamic.title("02 Each object associated with relatedResource MUST contain at least a digestSRI or a digestMultibase value.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=Each%20object%20associated%20with%20relatedResource%20MUST%20contain%20at%20least%20a%20digestSRI%20or%20a%20digestMultibase%20value.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("02 Advanced concepts")
    allure.dynamic.sub_suite("01 Integrity of related resources")
    pytest.skip("TBD")

def test_integrity_of_related_resources_3():
    allure.dynamic.title("03 The identifier for the resource is REQUIRED and conforms to the format defined in Section 4.4 Identifiers")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=The%20identifier%20for%20the%20resource%20is%20REQUIRED%20and%20conforms%20to%20the%20format%20defined%20in%20Section%204.4%20Identifiers", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("02 Advanced concepts")
    allure.dynamic.sub_suite("01 Integrity of related resources")
    pytest.skip("TBD")

def test_integrity_of_related_resources_4():
    allure.dynamic.title("04 The value MUST be unique among the list of related resource objects.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=The%20value%20MUST%20be%20unique%20among%20the%20list%20of%20related%20resource%20objects.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("02 Advanced concepts")
    allure.dynamic.sub_suite("01 Integrity of related resources")
    pytest.skip("TBD")

def test_integrity_of_related_resources_5():
    allure.dynamic.title("05 If it is, the specification MUST produce a validation error unless the resource matches the expected media type and cryptographic digest.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=If%20it%20is%2C%20the%20specification%20MUST%20produce%20a%20validation%20error%20unless%20the%20resource%20matches%20the%20expected%20media%20type%20and%20cryptographic%20digest.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("02 Advanced concepts")
    allure.dynamic.sub_suite("01 Integrity of related resources")
    pytest.skip("TBD")

def test_refreshing_0():
    allure.dynamic.title("00 The value of the refreshService property MUST be one or more refresh services that provides enough information to the recipient's software such that the recipient can refresh the verifiable credential")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=The%20value%20of%20the%20refreshService%20property%20MUST%20be%20one%20or%20more%20refresh%20services%20that%20provides%20enough%20information%20to%20the%20recipient%27s%20software%20such%20that%20the%20recipient%20can%20refresh%20the%20verifiable%20credential", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("02 Advanced concepts")
    allure.dynamic.sub_suite("02 Refreshing")
    pytest.skip("TBD")

def test_refreshing_1():
    allure.dynamic.title("01 Each refreshService value MUST specify its type")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=Each%20refreshService%20value%20MUST%20specify%20its%20type", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("02 Advanced concepts")
    allure.dynamic.sub_suite("02 Refreshing")
    pytest.skip("TBD")

def test_terms_of_use_0():
    allure.dynamic.title("00 The value of the termsOfUse property MUST specify one or more terms of use policies under which the creator issued the credential or presentation")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=The%20value%20of%20the%20termsOfUse%20property%20MUST%20specify%20one%20or%20more%20terms%20of%20use%20policies%20under%20which%20the%20creator%20issued%20the%20credential%20or%20presentation", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("02 Advanced concepts")
    allure.dynamic.sub_suite("03 Terms of use")
    pytest.skip("TBD")

def test_terms_of_use_1():
    allure.dynamic.title("01 Each termsOfUse value MUST specify its type, for example, TrustFrameworkPolicy, and MAY specify its instance id")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=Each%20termsOfUse%20value%20MUST%20specify%20its%20type%2C%20for%20example%2C%20TrustFrameworkPolicy%2C%20and%20MAY%20specify%20its%20instance%20id", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("02 Advanced concepts")
    allure.dynamic.sub_suite("03 Terms of use")
    pytest.skip("TBD")

def test_evidence_0():
    allure.dynamic.title("00 If present, the value of the evidence property MUST be either a single object or a set of one or more objects")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=If%20present%2C%20the%20value%20of%20the%20evidence%20property%20MUST%20be%20either%20a%20single%20object%20or%20a%20set%20of%20one%20or%20more%20objects", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("02 Advanced concepts")
    allure.dynamic.sub_suite("04 Evidence")
    pytest.skip("TBD")

def test_evidence_1():
    allure.dynamic.title("01 If present, the normative guidance in Section 4.4 Identifiers MUST be followed")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=If%20present%2C%20the%20normative%20guidance%20in%20Section%204.4%20Identifiers%20MUST%20be%20followed", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("02 Advanced concepts")
    allure.dynamic.sub_suite("04 Evidence")
    pytest.skip("TBD")

def test_evidence_2():
    allure.dynamic.title("02 type The type property is REQUIRED")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=type%20The%20type%20property%20is%20REQUIRED", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("02 Advanced concepts")
    allure.dynamic.sub_suite("04 Evidence")
    pytest.skip("TBD")

def test_evidence_3():
    allure.dynamic.title("03 The related normative guidance in Section 4.5 Types MUST be followed.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=The%20related%20normative%20guidance%20in%20Section%204.5%20Types%20MUST%20be%20followed.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("02 Advanced concepts")
    allure.dynamic.sub_suite("04 Evidence")
    pytest.skip("TBD")

def test_evidence_4():
    allure.dynamic.title("04 If present, the normative guidance in Section 4.4 Identifiers MUST be followed.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=If%20present%2C%20the%20normative%20guidance%20in%20Section%204.4%20Identifiers%20MUST%20be%20followed.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("02 Advanced concepts")
    allure.dynamic.sub_suite("04 Evidence")
    pytest.skip("TBD")

def test_evidence_5():
    allure.dynamic.title("05 The type property is REQUIRED")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=The%20type%20property%20is%20REQUIRED", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("02 Advanced concepts")
    allure.dynamic.sub_suite("04 Evidence")
    pytest.skip("TBD")

def test_zero_knowledge_proofs_0():
    allure.dynamic.title("00 Specification authors that create securing mechanisms MUST NOT design them in such a way that they leak information that would enable the verifier to correlate a holder across multiple verifiable presentations to different verifiers.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=Specification%20authors%20that%20create%20securing%20mechanisms%20MUST%20NOT%20design%20them%20in%20such%20a%20way%20that%20they%20leak%20information%20that%20would%20enable%20the%20verifier%20to%20correlate%20a%20holder%20across%20multiple%20verifiable%20presentations%20to%20different%20verifiers.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("02 Advanced concepts")
    allure.dynamic.sub_suite("05 Zero knowledge proofs")
    pytest.skip("TBD")

def test_representing_time_0():
    allure.dynamic.title("00 Time values that are incorrectly serialized without an offset MUST be interpreted as UTC")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=Time%20values%20that%20are%20incorrectly%20serialized%20without%20an%20offset%20MUST%20be%20interpreted%20as%20UTC", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("02 Advanced concepts")
    allure.dynamic.sub_suite("06 Representing time")
    pytest.skip("TBD")

def test_reserved_extension_points_0():
    allure.dynamic.title("00 In order to avoid collisions regarding how the following properties are used, implementations MUST specify a type property in the value associated with the reserved property")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=In%20order%20to%20avoid%20collisions%20regarding%20how%20the%20following%20properties%20are%20used%2C%20implementations%20MUST%20specify%20a%20type%20property%20in%20the%20value%20associated%20with%20the%20reserved%20property", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("02 Advanced concepts")
    allure.dynamic.sub_suite("07 Reserved extension points")
    pytest.skip("TBD")

def test_reserved_extension_points_1():
    allure.dynamic.title("01 The associated vocabulary URL MUST be https://www.w3.org/2018/credentials#confidenceMethod.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=The%20associated%20vocabulary%20URL%20MUST%20be%20https%3A//www.w3.org/2018/credentials%23confidenceMethod.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("02 Advanced concepts")
    allure.dynamic.sub_suite("07 Reserved extension points")
    pytest.skip("TBD")

def test_reserved_extension_points_2():
    allure.dynamic.title("02 The associated vocabulary URL MUST be https://www.w3.org/2018/credentials#renderMethod.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=The%20associated%20vocabulary%20URL%20MUST%20be%20https%3A//www.w3.org/2018/credentials%23renderMethod.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("02 Advanced concepts")
    allure.dynamic.sub_suite("07 Reserved extension points")
    pytest.skip("TBD")

def test_ecosystem_compatibility_0():
    allure.dynamic.title("00 MUST identify whether the transformation to this data model is one-way-only or round-trippable.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=MUST%20identify%20whether%20the%20transformation%20to%20this%20data%20model%20is%20one%2Dway%2Donly%20or%20round%2Dtrippable.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("02 Advanced concepts")
    allure.dynamic.sub_suite("08 Ecosystem compatibility")
    pytest.skip("TBD")

def test_ecosystem_compatibility_1():
    allure.dynamic.title("01 MUST preserve the @context values when performing round-trippable transformation.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=MUST%20preserve%20the%20%40context%20values%20when%20performing%20round%2Dtrippable%20transformation.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("02 Advanced concepts")
    allure.dynamic.sub_suite("08 Ecosystem compatibility")
    pytest.skip("TBD")

def test_ecosystem_compatibility_2():
    allure.dynamic.title("02 MUST result in a conforming document when transforming to the data model described by this specification.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=MUST%20result%20in%20a%20conforming%20document%20when%20transforming%20to%20the%20data%20model%20described%20by%20this%20specification.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("02 Advanced concepts")
    allure.dynamic.sub_suite("08 Ecosystem compatibility")
    pytest.skip("TBD")

def test_ecosystem_compatibility_3():
    allure.dynamic.title("03 MUST specify a registered media type for the input document.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=MUST%20specify%20a%20registered%20media%20type%20for%20the%20input%20document.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("02 Advanced concepts")
    allure.dynamic.sub_suite("08 Ecosystem compatibility")
    pytest.skip("TBD")

def test_securing_mechanism_specifications_0():
    allure.dynamic.title("00 Securing mechanism specifications MUST document normative algorithms that provide content integrity protection for conforming documents")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=Securing%20mechanism%20specifications%20MUST%20document%20normative%20algorithms%20that%20provide%20content%20integrity%20protection%20for%20conforming%20documents", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("02 Advanced concepts")
    allure.dynamic.sub_suite("09 Securing mechanism specifications")
    pytest.skip("TBD")

def test_securing_mechanism_specifications_1():
    allure.dynamic.title("01 Securing mechanism specifications MUST provide a verification algorithm that returns the information in the conforming document that has been secured, in isolation, without including any securing mechanism information, such as proof or JOSE/COSE header parameters and signatures")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=Securing%20mechanism%20specifications%20MUST%20provide%20a%20verification%20algorithm%20that%20returns%20the%20information%20in%20the%20conforming%20document%20that%20has%20been%20secured%2C%20in%20isolation%2C%20without%20including%20any%20securing%20mechanism%20information%2C%20such%20as%20proof%20or%20JOSE/COSE%20header%20parameters%20and%20signatures", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("02 Advanced concepts")
    allure.dynamic.sub_suite("09 Securing mechanism specifications")
    pytest.skip("TBD")

def test_securing_mechanism_specifications_2():
    allure.dynamic.title("02 A verification algorithm MUST provide an interface that receives a media type (string inputMediaType) and input data (byte sequence or map inputData)")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=A%20verification%20algorithm%20MUST%20provide%20an%20interface%20that%20receives%20a%20media%20type%20%28string%20inputMediaType%29%20and%20input%20data%20%28byte%20sequence%20or%20map%20inputData%29", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("02 Advanced concepts")
    allure.dynamic.sub_suite("09 Securing mechanism specifications")
    pytest.skip("TBD")

def test_securing_mechanism_specifications_3():
    allure.dynamic.title("03 A securing mechanism specification that creates a new type of embedded proof MUST specify a property that relates the verifiable credential or verifiable presentation to a proof graph")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=A%20securing%20mechanism%20specification%20that%20creates%20a%20new%20type%20of%20embedded%20proof%20MUST%20specify%20a%20property%20that%20relates%20the%20verifiable%20credential%20or%20verifiable%20presentation%20to%20a%20proof%20graph", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("02 Advanced concepts")
    allure.dynamic.sub_suite("09 Securing mechanism specifications")
    pytest.skip("TBD")

def test_securing_mechanism_specifications_4():
    allure.dynamic.title("04 The securing mechanism MUST define all terms used by the proof graph")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=The%20securing%20mechanism%20MUST%20define%20all%20terms%20used%20by%20the%20proof%20graph", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("02 Advanced concepts")
    allure.dynamic.sub_suite("09 Securing mechanism specifications")
    pytest.skip("TBD")

def test_securing_mechanism_specifications_5():
    allure.dynamic.title("05 The securing mechanism MUST secure all graphs in the verifiable credential or the verifiable presentation, except for any proof graphs securing the verifiable credential or the verifiable presentation itself.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=The%20securing%20mechanism%20MUST%20secure%20all%20graphs%20in%20the%20verifiable%20credential%20or%20the%20verifiable%20presentation%2C%20except%20for%20any%20proof%20graphs%20securing%20the%20verifiable%20credential%20or%20the%20verifiable%20presentation%20itself.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("02 Advanced concepts")
    allure.dynamic.sub_suite("09 Securing mechanism specifications")
    pytest.skip("TBD")

def test_json_ld_0():
    allure.dynamic.title("00 JSON-LD compacted document form MUST be utilized for all representations of the data model using the application/vc or application/vp media type.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=JSON%2DLD%20compacted%20document%20form%20MUST%20be%20utilized%20for%20all%20representations%20of%20the%20data%20model%20using%20the%20application/vc%20or%20application/vp%20media%20type.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("03 Syntaxes")
    allure.dynamic.sub_suite("00 Json ld")
    pytest.skip("TBD")

def test_verification_0():
    allure.dynamic.title("00 This section contains an algorithm that conforming verifier implementations MUST run when verifying a verifiable credential or a verifiable presentation")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=This%20section%20contains%20an%20algorithm%20that%20conforming%20verifier%20implementations%20MUST%20run%20when%20verifying%20a%20verifiable%20credential%20or%20a%20verifiable%20presentation", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("04 Algorithms")
    allure.dynamic.sub_suite("00 Verification")
    pytest.skip("TBD")

def test_verification_1():
    allure.dynamic.title("01 The verifyProof function MUST implement the interface described in 5.13 Securing Mechanism Specifications.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=The%20verifyProof%20function%20MUST%20implement%20the%20interface%20described%20in%205.13%20Securing%20Mechanism%20Specifications.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("04 Algorithms")
    allure.dynamic.sub_suite("00 Verification")
    pytest.skip("TBD")

def test_problem_details_0():
    allure.dynamic.title("00 The type property MUST be present and its value MUST be a URL identifying the type of problem.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=The%20type%20property%20MUST%20be%20present%20and%20its%20value%20MUST%20be%20a%20URL%20identifying%20the%20type%20of%20problem.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("04 Algorithms")
    allure.dynamic.sub_suite("01 Problem details")
    pytest.skip("TBD")

def test_problem_details_1():
    allure.dynamic.title("01 If present, its value MUST be an integer that identifies the type of the problem")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=If%20present%2C%20its%20value%20MUST%20be%20an%20integer%20that%20identifies%20the%20type%20of%20the%20problem", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("04 Algorithms")
    allure.dynamic.sub_suite("01 Problem details")
    pytest.skip("TBD")

def test_problem_details_2():
    allure.dynamic.title("02 The title property MUST be present and its value SHOULD provide a short but specific human-readable string for the problem.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=The%20title%20property%20MUST%20be%20present%20and%20its%20value%20SHOULD%20provide%20a%20short%20but%20specific%20human%2Dreadable%20string%20for%20the%20problem.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("04 Algorithms")
    allure.dynamic.sub_suite("01 Problem details")
    pytest.skip("TBD")

def test_problem_details_3():
    allure.dynamic.title("03 The detail property MUST be present and its value SHOULD provide a longer human-readable string for the problem.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=The%20detail%20property%20MUST%20be%20present%20and%20its%20value%20SHOULD%20provide%20a%20longer%20human%2Dreadable%20string%20for%20the%20problem.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("04 Algorithms")
    allure.dynamic.sub_suite("01 Problem details")
    pytest.skip("TBD")

def test_language_and_base_direction_0():
    allure.dynamic.title("00 When the language value object is used in place of a string value, the object MUST contain a @value property whose value is a string, and SHOULD contain a @language property whose value is a string containing a well-formed Language-Tag as defined by [BCP47], and MAY contain a @direction property whose value is a base direction string defined by the @direction property in [JSON-LD11]")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=When%20the%20language%20value%20object%20is%20used%20in%20place%20of%20a%20string%20value%2C%20the%20object%20MUST%20contain%20a%20%40value%20property%20whose%20value%20is%20a%20string%2C%20and%20SHOULD%20contain%20a%20%40language%20property%20whose%20value%20is%20a%20string%20containing%20a%20well%2Dformed%20Language%2DTag%20as%20defined%20by%20%5BBCP47%5D%2C%20and%20MAY%20contain%20a%20%40direction%20property%20whose%20value%20is%20a%20base%20direction%20string%20defined%20by%20the%20%40direction%20property%20in%20%5BJSON%2DLD11%5D", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("05 Internationalization considerations")
    allure.dynamic.sub_suite("00 Language and base direction")
    pytest.skip("TBD")

def test_language_and_base_direction_1():
    allure.dynamic.title("01 The language value object MUST NOT include any other keys beyond @value, @language, and @direction.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=The%20language%20value%20object%20MUST%20NOT%20include%20any%20other%20keys%20beyond%20%40value%2C%20%40language%2C%20and%20%40direction.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("05 Internationalization considerations")
    allure.dynamic.sub_suite("00 Language and base direction")
    pytest.skip("TBD")

def test_base_context_0():
    allure.dynamic.title("00 Implementations MUST treat the base context value, located at https://www.w3.org/ns/credentials/v2, as already retrieved; the following value is the hexadecimal encoded SHA2-256 digest value of the base context file: 24a18c90e9856d526111f29376e302d970b2bd10182e33959995b0207d7043b9")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=Implementations%20MUST%20treat%20the%20base%20context%20value%2C%20located%20at%20https%3A//www.w3.org/ns/credentials/v2%2C%20as%20already%20retrieved%3B%20the%20following%20value%20is%20the%20hexadecimal%20encoded%20SHA2%2D256%20digest%20value%20of%20the%20base%20context%20file%3A%2024a18c90e9856d526111f29376e302d970b2bd10182e33959995b0207d7043b9", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("06 Contexts vocabularies types and credential schemas")
    allure.dynamic.sub_suite("00 Base context")
    pytest.skip("TBD")

def test_base_context_1():
    allure.dynamic.title("01 If such operations are performed and result in an error, the verifiable credential or verifiable presentation MUST result in a verification failure.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=If%20such%20operations%20are%20performed%20and%20result%20in%20an%20error%2C%20the%20verifiable%20credential%20or%20verifiable%20presentation%20MUST%20result%20in%20a%20verification%20failure.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("06 Contexts vocabularies types and credential schemas")
    allure.dynamic.sub_suite("00 Base context")
    pytest.skip("TBD")

def test_vocabularies_0():
    allure.dynamic.title("00 Implementations that depend on RDF vocabulary processing MUST ensure that the following vocabulary URLs used in the base context ultimately resolve to the following files when loading the JSON-LD serializations, which are normative")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-model-2.0/#:~:text=Implementations%20that%20depend%20on%20RDF%20vocabulary%20processing%20MUST%20ensure%20that%20the%20following%20vocabulary%20URLs%20used%20in%20the%20base%20context%20ultimately%20resolve%20to%20the%20following%20files%20when%20loading%20the%20JSON%2DLD%20serializations%2C%20which%20are%20normative", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credentials Data Model v2.0")
    allure.dynamic.suite("06 Contexts vocabularies types and credential schemas")
    allure.dynamic.sub_suite("01 Vocabularies")
    pytest.skip("TBD")
