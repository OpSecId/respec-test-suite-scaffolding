import allure
import pytest

def test_conformance_0():
    allure.dynamic.title("00 The key words MAY, MUST, OPTIONAL, and SHOULD in this document are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all capitals, as shown here.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-integrity/#:~:text=The%20key%20words%20MAY%2C%20MUST%2C%20OPTIONAL%2C%20and%20SHOULD%20in%20this%20document%20are%20to%20be%20interpreted%20as%20described%20in%20BCP%2014%20%5BRFC2119%5D%20%5BRFC8174%5D%20when%2C%20and%20only%20when%2C%20they%20appear%20in%20all%20capitals%2C%20as%20shown%20here.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credential Data Integrity 1.0")
    allure.dynamic.suite("00 Introduction")
    allure.dynamic.sub_suite("00 Conformance")
    pytest.skip("TBD")

def test_conformance_1():
    allure.dynamic.title("01 Conforming processors MUST produce errors when non-conforming documents are consumed.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-integrity/#:~:text=Conforming%20processors%20MUST%20produce%20errors%20when%20non%2Dconforming%20documents%20are%20consumed.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credential Data Integrity 1.0")
    allure.dynamic.suite("00 Introduction")
    allure.dynamic.sub_suite("00 Conformance")
    pytest.skip("TBD")

def test_proofs_0():
    allure.dynamic.title("00 When expressing a data integrity proof on an object, a proof property MUST be used")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-integrity/#:~:text=When%20expressing%20a%20data%20integrity%20proof%20on%20an%20object%2C%20a%20proof%20property%20MUST%20be%20used", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credential Data Integrity 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("00 Proofs")
    pytest.skip("TBD")

def test_proofs_1():
    allure.dynamic.title("01 If present, its value MUST be either a single object, or an unordered set of objects, expressed using the properties below:")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-integrity/#:~:text=If%20present%2C%20its%20value%20MUST%20be%20either%20a%20single%20object%2C%20or%20an%20unordered%20set%20of%20objects%2C%20expressed%20using%20the%20properties%20below%3A", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credential Data Integrity 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("00 Proofs")
    pytest.skip("TBD")

def test_proofs_2():
    allure.dynamic.title("02 An optional identifier for the proof, which MUST be a URL [URL], such as a UUID as a URN (urn:uuid:6a1676b8-b51f-11ed-937b-d76685a20ff5)")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-integrity/#:~:text=An%20optional%20identifier%20for%20the%20proof%2C%20which%20MUST%20be%20a%20URL%20%5BURL%5D%2C%20such%20as%20a%20UUID%20as%20a%20URN%20%28urn%3Auuid%3A6a1676b8%2Db51f%2D11ed%2D937b%2Dd76685a20ff5%29", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credential Data Integrity 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("00 Proofs")
    pytest.skip("TBD")

def test_proofs_3():
    allure.dynamic.title("03 The specific type of proof MUST be specified as a string that maps to a URL [URL]")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-integrity/#:~:text=The%20specific%20type%20of%20proof%20MUST%20be%20specified%20as%20a%20string%20that%20maps%20to%20a%20URL%20%5BURL%5D", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credential Data Integrity 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("00 Proofs")
    pytest.skip("TBD")

def test_proofs_4():
    allure.dynamic.title("04 The reason the proof was created MUST be specified as a string that maps to a URL [URL]")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-integrity/#:~:text=The%20reason%20the%20proof%20was%20created%20MUST%20be%20specified%20as%20a%20string%20that%20maps%20to%20a%20URL%20%5BURL%5D", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credential Data Integrity 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("00 Proofs")
    pytest.skip("TBD")

def test_proofs_5():
    allure.dynamic.title("05 If included, the value MUST be a string that maps to a [URL]")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-integrity/#:~:text=If%20included%2C%20the%20value%20MUST%20be%20a%20string%20that%20maps%20to%20a%20%5BURL%5D", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credential Data Integrity 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("00 Proofs")
    pytest.skip("TBD")

def test_proofs_6():
    allure.dynamic.title("06 If the proof type is DataIntegrityProof, cryptosuite MUST be specified; otherwise, cryptosuite MAY be specified")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-integrity/#:~:text=If%20the%20proof%20type%20is%20DataIntegrityProof%2C%20cryptosuite%20MUST%20be%20specified%3B%20otherwise%2C%20cryptosuite%20MAY%20be%20specified", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credential Data Integrity 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("00 Proofs")
    pytest.skip("TBD")

def test_proofs_7():
    allure.dynamic.title("07 If specified, its value MUST be a string.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-integrity/#:~:text=If%20specified%2C%20its%20value%20MUST%20be%20a%20string.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credential Data Integrity 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("00 Proofs")
    pytest.skip("TBD")

def test_proofs_8():
    allure.dynamic.title("08 The date and time the proof was created is OPTIONAL and, if included, MUST be specified as an [XMLSCHEMA11-2] dateTimeStamp string, either in Universal Coordinated Time (UTC), denoted by a Z at the end of the value, or with a time zone offset relative to UTC")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-integrity/#:~:text=The%20date%20and%20time%20the%20proof%20was%20created%20is%20OPTIONAL%20and%2C%20if%20included%2C%20MUST%20be%20specified%20as%20an%20%5BXMLSCHEMA11%2D2%5D%20dateTimeStamp%20string%2C%20either%20in%20Universal%20Coordinated%20Time%20%28UTC%29%2C%20denoted%20by%20a%20Z%20at%20the%20end%20of%20the%20value%2C%20or%20with%20a%20time%20zone%20offset%20relative%20to%20UTC", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credential Data Integrity 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("00 Proofs")
    pytest.skip("TBD")

def test_proofs_9():
    allure.dynamic.title("09 If present, it MUST be an [XMLSCHEMA11-2] dateTimeStamp string, either in Universal Coordinated Time (UTC), denoted by a Z at the end of the value, or with a time zone offset relative to UTC")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-integrity/#:~:text=If%20present%2C%20it%20MUST%20be%20an%20%5BXMLSCHEMA11%2D2%5D%20dateTimeStamp%20string%2C%20either%20in%20Universal%20Coordinated%20Time%20%28UTC%29%2C%20denoted%20by%20a%20Z%20at%20the%20end%20of%20the%20value%2C%20or%20with%20a%20time%20zone%20offset%20relative%20to%20UTC", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credential Data Integrity 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("00 Proofs")
    pytest.skip("TBD")

def test_proofs_10():
    allure.dynamic.title("10 If specified, the associated value MUST be either a string, or an unordered set of strings")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-integrity/#:~:text=If%20specified%2C%20the%20associated%20value%20MUST%20be%20either%20a%20string%2C%20or%20an%20unordered%20set%20of%20strings", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credential Data Integrity 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("00 Proofs")
    pytest.skip("TBD")

def test_proofs_11():
    allure.dynamic.title("11 The value MUST use a header and encoding as described in Section 2.4 Multibase of the Controller Documents 1.0 specification to express the binary data")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-integrity/#:~:text=The%20value%20MUST%20use%20a%20header%20and%20encoding%20as%20described%20in%20Section%202.4%20Multibase%20of%20the%20Controller%20Documents%201.0%20specification%20to%20express%20the%20binary%20data", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credential Data Integrity 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("00 Proofs")
    pytest.skip("TBD")

def test_proofs_12():
    allure.dynamic.title("12 Each value identifies another data integrity proof that MUST verify before the current proof is processed")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-integrity/#:~:text=Each%20value%20identifies%20another%20data%20integrity%20proof%20that%20MUST%20verify%20before%20the%20current%20proof%20is%20processed", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credential Data Integrity 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("00 Proofs")
    pytest.skip("TBD")

def test_proofs_13():
    allure.dynamic.title("13 If an unordered list, all referenced proofs in the array MUST verify")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-integrity/#:~:text=If%20an%20unordered%20list%2C%20all%20referenced%20proofs%20in%20the%20array%20MUST%20verify", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credential Data Integrity 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("00 Proofs")
    pytest.skip("TBD")

def test_resource_integrity_0():
    allure.dynamic.title("00 If present, the digestMultibase value MUST be a single string value, or an array of string values, each of which is a Multibase-encoded Multihash value.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-integrity/#:~:text=If%20present%2C%20the%20digestMultibase%20value%20MUST%20be%20a%20single%20string%20value%2C%20or%20an%20array%20of%20string%20values%2C%20each%20of%20which%20is%20a%20Multibase%2Dencoded%20Multihash%20value.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credential Data Integrity 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("01 Resource integrity")
    pytest.skip("TBD")

def test_contexts_and_vocabularies_0():
    allure.dynamic.title("00 Implementations that perform JSON-LD processing MUST treat the following JSON-LD context URLs as already resolved, where the resolved document matches the corresponding hash values below:")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-integrity/#:~:text=Implementations%20that%20perform%20JSON%2DLD%20processing%20MUST%20treat%20the%20following%20JSON%2DLD%20context%20URLs%20as%20already%20resolved%2C%20where%20the%20resolved%20document%20matches%20the%20corresponding%20hash%20values%20below%3A", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credential Data Integrity 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("02 Contexts and vocabularies")
    pytest.skip("TBD")

def test_contexts_and_vocabularies_1():
    allure.dynamic.title("01 Implementations that perform RDF processing MUST treat the JSON-LD serialization of the vocabulary URL as already dereferenced, where the dereferenced document matches the corresponding hash value below.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-integrity/#:~:text=Implementations%20that%20perform%20RDF%20processing%20MUST%20treat%20the%20JSON%2DLD%20serialization%20of%20the%20vocabulary%20URL%20as%20already%20dereferenced%2C%20where%20the%20dereferenced%20document%20matches%20the%20corresponding%20hash%20value%20below.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credential Data Integrity 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("02 Contexts and vocabularies")
    pytest.skip("TBD")

def test_contexts_and_vocabularies_2():
    allure.dynamic.title("02 Applications MUST use the algorithm in Section 4.6 Context Validation, or one that achieves equivalent protections, to validate contexts in a conforming secured document")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-integrity/#:~:text=Applications%20MUST%20use%20the%20algorithm%20in%20Section%204.6%20Context%20Validation%2C%20or%20one%20that%20achieves%20equivalent%20protections%2C%20to%20validate%20contexts%20in%20a%20conforming%20secured%20document", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credential Data Integrity 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("02 Contexts and vocabularies")
    pytest.skip("TBD")

def test_contexts_and_vocabularies_3():
    allure.dynamic.title("03 Context validation MUST be run after running the applicable algorithm in either Section 4.4 Verify Proof or Section 4.5 Verify Proof Sets and Chains.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-integrity/#:~:text=Context%20validation%20MUST%20be%20run%20after%20running%20the%20applicable%20algorithm%20in%20either%20Section%204.4%20Verify%20Proof%20or%20Section%204.5%20Verify%20Proof%20Sets%20and%20Chains.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credential Data Integrity 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("02 Contexts and vocabularies")
    pytest.skip("TBD")

def test_contexts_and_vocabularies_4():
    allure.dynamic.title("04 When securing a document, if an @context property is not provided in the document or the Data Integrity terms used in the document are not mapped by existing values in the @context property, implementations MUST inject or add an @context property with a value of https://w3id.org/security/data-integrity/v2.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-integrity/#:~:text=When%20securing%20a%20document%2C%20if%20an%20%40context%20property%20is%20not%20provided%20in%20the%20document%20or%20the%20Data%20Integrity%20terms%20used%20in%20the%20document%20are%20not%20mapped%20by%20existing%20values%20in%20the%20%40context%20property%2C%20implementations%20MUST%20inject%20or%20add%20an%20%40context%20property%20with%20a%20value%20of%20https%3A//w3id.org/security/data%2Dintegrity/v2.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credential Data Integrity 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("02 Contexts and vocabularies")
    pytest.skip("TBD")

def test_contexts_and_vocabularies_5():
    allure.dynamic.title("05 Implementations that use JSON-LD processing, such as RDF Dataset Canonicalization [RDF-CANON], MUST throw an error, which SHOULD be DATA_LOSS_DETECTION_ERROR, when data is dropped by a JSON-LD processor, such as when an undefined term is detected in an input document.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-integrity/#:~:text=Implementations%20that%20use%20JSON%2DLD%20processing%2C%20such%20as%20RDF%20Dataset%20Canonicalization%20%5BRDF%2DCANON%5D%2C%20MUST%20throw%20an%20error%2C%20which%20SHOULD%20be%20DATA_LOSS_DETECTION_ERROR%2C%20when%20data%20is%20dropped%20by%20a%20JSON%2DLD%20processor%2C%20such%20as%20when%20an%20undefined%20term%20is%20detected%20in%20an%20input%20document.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credential Data Integrity 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("02 Contexts and vocabularies")
    pytest.skip("TBD")

def test_contexts_and_vocabularies_6():
    allure.dynamic.title("06 When deserializing to RDF, implementations MUST ensure that the base URL is set to null.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-integrity/#:~:text=When%20deserializing%20to%20RDF%2C%20implementations%20MUST%20ensure%20that%20the%20base%20URL%20is%20set%20to%20null.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credential Data Integrity 1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("02 Contexts and vocabularies")
    pytest.skip("TBD")

def test_dataintegrityproof_0():
    allure.dynamic.title("00 The type property MUST contain the string DataIntegrityProof.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-integrity/#:~:text=The%20type%20property%20MUST%20contain%20the%20string%20DataIntegrityProof.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credential Data Integrity 1.0")
    allure.dynamic.suite("02 Cryptographic suites")
    allure.dynamic.sub_suite("00 Dataintegrityproof")
    pytest.skip("TBD")

def test_dataintegrityproof_1():
    allure.dynamic.title("01 The value of the cryptosuite property MUST be a string that identifies the cryptographic suite")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-integrity/#:~:text=The%20value%20of%20the%20cryptosuite%20property%20MUST%20be%20a%20string%20that%20identifies%20the%20cryptographic%20suite", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credential Data Integrity 1.0")
    allure.dynamic.suite("02 Cryptographic suites")
    allure.dynamic.sub_suite("00 Dataintegrityproof")
    pytest.skip("TBD")

def test_dataintegrityproof_2():
    allure.dynamic.title("02 If the processing environment supports subtypes of string, the type of the cryptosuite value MUST be the https://w3id.org/security#cryptosuiteString subtype of string.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-integrity/#:~:text=If%20the%20processing%20environment%20supports%20subtypes%20of%20string%2C%20the%20type%20of%20the%20cryptosuite%20value%20MUST%20be%20the%20https%3A//w3id.org/security%23cryptosuiteString%20subtype%20of%20string.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credential Data Integrity 1.0")
    allure.dynamic.suite("02 Cryptographic suites")
    allure.dynamic.sub_suite("00 Dataintegrityproof")
    pytest.skip("TBD")

def test_dataintegrityproof_3():
    allure.dynamic.title("03 The proofValue property MUST be used, as specified in 2.1 Proofs.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-integrity/#:~:text=The%20proofValue%20property%20MUST%20be%20used%2C%20as%20specified%20in%202.1%20Proofs.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credential Data Integrity 1.0")
    allure.dynamic.suite("02 Cryptographic suites")
    allure.dynamic.sub_suite("00 Dataintegrityproof")
    pytest.skip("TBD")

def test_dataintegrityproof_4():
    allure.dynamic.title("04 Cryptographic suite designers MUST use mandatory proof value properties defined in Section 2.1 Proofs, and MAY define other properties specific to their cryptographic suite.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-integrity/#:~:text=Cryptographic%20suite%20designers%20MUST%20use%20mandatory%20proof%20value%20properties%20defined%20in%20Section%202.1%20Proofs%2C%20and%20MAY%20define%20other%20properties%20specific%20to%20their%20cryptographic%20suite.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credential Data Integrity 1.0")
    allure.dynamic.suite("02 Cryptographic suites")
    allure.dynamic.sub_suite("00 Dataintegrityproof")
    pytest.skip("TBD")

def test_add_proof_0():
    allure.dynamic.title("00 Whenever this algorithm encodes strings, it MUST use UTF-8 encoding.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-integrity/#:~:text=Whenever%20this%20algorithm%20encodes%20strings%2C%20it%20MUST%20use%20UTF%2D8%20encoding.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credential Data Integrity 1.0")
    allure.dynamic.suite("03 Algorithms")
    allure.dynamic.sub_suite("00 Add proof")
    pytest.skip("TBD")

def test_add_proof_1():
    allure.dynamic.title("01 If the algorithm produces an error, the error MUST be propagated and SHOULD convey the error type.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-integrity/#:~:text=If%20the%20algorithm%20produces%20an%20error%2C%20the%20error%20MUST%20be%20propagated%20and%20SHOULD%20convey%20the%20error%20type.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credential Data Integrity 1.0")
    allure.dynamic.suite("03 Algorithms")
    allure.dynamic.sub_suite("00 Add proof")
    pytest.skip("TBD")

def test_add_proof_2():
    allure.dynamic.title("02 If one or more of the proof.type, proof.verificationMethod, and proof.proofPurpose values is not set, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-integrity/#:~:text=If%20one%20or%20more%20of%20the%20proof.type%2C%20proof.verificationMethod%2C%20and%20proof.proofPurpose%20values%20is%20not%20set%2C%20an%20error%20MUST%20be%20raised%20and%20SHOULD%20convey%20an%20error%20type%20of%20PROOF_GENERATION_ERROR.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credential Data Integrity 1.0")
    allure.dynamic.suite("03 Algorithms")
    allure.dynamic.sub_suite("00 Add proof")
    pytest.skip("TBD")

def test_add_proof_3():
    allure.dynamic.title("03 If options has a non-null domain item, it MUST be equal to proof.domain or an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-integrity/#:~:text=If%20options%20has%20a%20non%2Dnull%20domain%20item%2C%20it%20MUST%20be%20equal%20to%20proof.domain%20or%20an%20error%20MUST%20be%20raised%20and%20SHOULD%20convey%20an%20error%20type%20of%20PROOF_GENERATION_ERROR.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credential Data Integrity 1.0")
    allure.dynamic.suite("03 Algorithms")
    allure.dynamic.sub_suite("00 Add proof")
    pytest.skip("TBD")

def test_add_proof_4():
    allure.dynamic.title("04 If options has a non-null challenge item, it MUST be equal to proof.challenge or an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-integrity/#:~:text=If%20options%20has%20a%20non%2Dnull%20challenge%20item%2C%20it%20MUST%20be%20equal%20to%20proof.challenge%20or%20an%20error%20MUST%20be%20raised%20and%20SHOULD%20convey%20an%20error%20type%20of%20PROOF_GENERATION_ERROR.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credential Data Integrity 1.0")
    allure.dynamic.suite("03 Algorithms")
    allure.dynamic.sub_suite("00 Add proof")
    pytest.skip("TBD")

def test_add_proof_set_chain_0():
    allure.dynamic.title("00 Whenever this algorithm encodes strings, it MUST use UTF-8 encoding.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-integrity/#:~:text=Whenever%20this%20algorithm%20encodes%20strings%2C%20it%20MUST%20use%20UTF%2D8%20encoding.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credential Data Integrity 1.0")
    allure.dynamic.suite("03 Algorithms")
    allure.dynamic.sub_suite("01 Add proof set chain")
    pytest.skip("TBD")

def test_add_proof_set_chain_1():
    allure.dynamic.title("01 If a proof with id equal to previousProof does not exist in allProofs, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-integrity/#:~:text=If%20a%20proof%20with%20id%20equal%20to%20previousProof%20does%20not%20exist%20in%20allProofs%2C%20an%20error%20MUST%20be%20raised%20and%20SHOULD%20convey%20an%20error%20type%20of%20PROOF_GENERATION_ERROR.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credential Data Integrity 1.0")
    allure.dynamic.suite("03 Algorithms")
    allure.dynamic.sub_suite("01 Add proof set chain")
    pytest.skip("TBD")

def test_add_proof_set_chain_2():
    allure.dynamic.title("02 If any element of previousProof array has an id attribute that does not match the id attribute of any element of allProofs, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-integrity/#:~:text=If%20any%20element%20of%20previousProof%20array%20has%20an%20id%20attribute%20that%20does%20not%20match%20the%20id%20attribute%20of%20any%20element%20of%20allProofs%2C%20an%20error%20MUST%20be%20raised%20and%20SHOULD%20convey%20an%20error%20type%20of%20PROOF_GENERATION_ERROR.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credential Data Integrity 1.0")
    allure.dynamic.suite("03 Algorithms")
    allure.dynamic.sub_suite("01 Add proof set chain")
    pytest.skip("TBD")

def test_verify_proof_0():
    allure.dynamic.title("00 When a step says 'an error MUST be raised', it means that a verification result MUST be returned with a verified of false and a non-empty errors list.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-integrity/#:~:text=When%20a%20step%20says%20%27an%20error%20MUST%20be%20raised%27%2C%20it%20means%20that%20a%20verification%20result%20MUST%20be%20returned%20with%20a%20verified%20of%20false%20and%20a%20non%2Dempty%20errors%20list.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credential Data Integrity 1.0")
    allure.dynamic.suite("03 Algorithms")
    allure.dynamic.sub_suite("02 Verify proof")
    pytest.skip("TBD")

def test_verify_proof_1():
    allure.dynamic.title("01 If either securedDocument is not a map or securedDocument.proof is not a map, an error MUST be raised and SHOULD convey an error type of PARSING_ERROR.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-integrity/#:~:text=If%20either%20securedDocument%20is%20not%20a%20map%20or%20securedDocument.proof%20is%20not%20a%20map%2C%20an%20error%20MUST%20be%20raised%20and%20SHOULD%20convey%20an%20error%20type%20of%20PARSING_ERROR.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credential Data Integrity 1.0")
    allure.dynamic.suite("03 Algorithms")
    allure.dynamic.sub_suite("02 Verify proof")
    pytest.skip("TBD")

def test_verify_proof_2():
    allure.dynamic.title("02 If one or more of proof.type, proof.verificationMethod, and proof.proofPurpose does not exist, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-integrity/#:~:text=If%20one%20or%20more%20of%20proof.type%2C%20proof.verificationMethod%2C%20and%20proof.proofPurpose%20does%20not%20exist%2C%20an%20error%20MUST%20be%20raised%20and%20SHOULD%20convey%20an%20error%20type%20of%20PROOF_VERIFICATION_ERROR.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credential Data Integrity 1.0")
    allure.dynamic.suite("03 Algorithms")
    allure.dynamic.sub_suite("02 Verify proof")
    pytest.skip("TBD")

def test_verify_proof_3():
    allure.dynamic.title("03 If expectedProofPurpose was given, and it does not match proof.proofPurpose, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-integrity/#:~:text=If%20expectedProofPurpose%20was%20given%2C%20and%20it%20does%20not%20match%20proof.proofPurpose%2C%20an%20error%20MUST%20be%20raised%20and%20SHOULD%20convey%20an%20error%20type%20of%20PROOF_VERIFICATION_ERROR.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credential Data Integrity 1.0")
    allure.dynamic.suite("03 Algorithms")
    allure.dynamic.sub_suite("02 Verify proof")
    pytest.skip("TBD")

def test_verify_proof_4():
    allure.dynamic.title("04 If domain was given, and it does not contain the same strings as proof.domain (treating a single string as a set containing just that string), an error MUST be raised and SHOULD convey an error type of INVALID_DOMAIN_ERROR.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-integrity/#:~:text=If%20domain%20was%20given%2C%20and%20it%20does%20not%20contain%20the%20same%20strings%20as%20proof.domain%20%28treating%20a%20single%20string%20as%20a%20set%20containing%20just%20that%20string%29%2C%20an%20error%20MUST%20be%20raised%20and%20SHOULD%20convey%20an%20error%20type%20of%20INVALID_DOMAIN_ERROR.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credential Data Integrity 1.0")
    allure.dynamic.suite("03 Algorithms")
    allure.dynamic.sub_suite("02 Verify proof")
    pytest.skip("TBD")

def test_verify_proof_5():
    allure.dynamic.title("05 If challenge was given, and it does not match proof.challenge, an error MUST be raised and SHOULD convey an error type of INVALID_CHALLENGE_ERROR.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-integrity/#:~:text=If%20challenge%20was%20given%2C%20and%20it%20does%20not%20match%20proof.challenge%2C%20an%20error%20MUST%20be%20raised%20and%20SHOULD%20convey%20an%20error%20type%20of%20INVALID_CHALLENGE_ERROR.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credential Data Integrity 1.0")
    allure.dynamic.suite("03 Algorithms")
    allure.dynamic.sub_suite("02 Verify proof")
    pytest.skip("TBD")

def test_verify_proof_sets_and_chains_0():
    allure.dynamic.title("00 If a proof with id does not exist in allProofs, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-integrity/#:~:text=If%20a%20proof%20with%20id%20does%20not%20exist%20in%20allProofs%2C%20an%20error%20MUST%20be%20raised%20and%20SHOULD%20convey%20an%20error%20type%20of%20PROOF_VERIFICATION_ERROR", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credential Data Integrity 1.0")
    allure.dynamic.suite("03 Algorithms")
    allure.dynamic.sub_suite("03 Verify proof sets and chains")
    pytest.skip("TBD")

def test_verify_proof_sets_and_chains_1():
    allure.dynamic.title("01 If any element of previousProof array has an id attribute that does not match the id attribute of any element of allProofs, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-integrity/#:~:text=If%20any%20element%20of%20previousProof%20array%20has%20an%20id%20attribute%20that%20does%20not%20match%20the%20id%20attribute%20of%20any%20element%20of%20allProofs%2C%20an%20error%20MUST%20be%20raised%20and%20SHOULD%20convey%20an%20error%20type%20of%20PROOF_VERIFICATION_ERROR.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credential Data Integrity 1.0")
    allure.dynamic.suite("03 Algorithms")
    allure.dynamic.sub_suite("03 Verify proof sets and chains")
    pytest.skip("TBD")

def test_processing_errors_0():
    allure.dynamic.title("00 The type value of the error object MUST be a URL that starts with the value https://w3id.org/security# and ends with the value in the section listed below.")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-integrity/#:~:text=The%20type%20value%20of%20the%20error%20object%20MUST%20be%20a%20URL%20that%20starts%20with%20the%20value%20https%3A//w3id.org/security%23%20and%20ends%20with%20the%20value%20in%20the%20section%20listed%20below.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credential Data Integrity 1.0")
    allure.dynamic.suite("03 Algorithms")
    allure.dynamic.sub_suite("04 Processing errors")
    pytest.skip("TBD")

def test_processing_errors_1():
    allure.dynamic.title("01 The code value MUST be the integer code described in the table below (in parentheses, beside the type name).")
    allure.dynamic.link("https://www.w3.org/TR/vc-data-integrity/#:~:text=The%20code%20value%20MUST%20be%20the%20integer%20code%20described%20in%20the%20table%20below%20%28in%20parentheses%2C%20beside%20the%20type%20name%29.", name="Specification")
    allure.dynamic.parent_suite("Verifiable Credential Data Integrity 1.0")
    allure.dynamic.suite("03 Algorithms")
    allure.dynamic.sub_suite("04 Processing errors")
    pytest.skip("TBD")
