import allure
import pytest

def test_conformance_0():
    allure.dynamic.title("00 The key words MAY, MUST, MUST NOT, and SHOULD in this document are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all capitals, as shown here.")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-eddsa/#:~:text=The%20key%20words%20MAY%2C%20MUST%2C%20MUST%20NOT%2C%20and%20SHOULD%20in%20this%20document%20are%20to%20be%20interpreted%20as%20described%20in%20BCP%2014%20%5BRFC2119%5D%20%5BRFC8174%5D%20when%2C%20and%20only%20when%2C%20they%20appear%20in%20all%20capitals%2C%20as%20shown%20here.", name="Specification")
    allure.dynamic.parent_suite("Data Integrity EdDSA Cryptosuites v1.0")
    allure.dynamic.suite("00 Introduction")
    allure.dynamic.sub_suite("00 Conformance")
    pytest.skip("TBD")

def test_conformance_1():
    allure.dynamic.title("01 Algorithms of this document MUST be enforced.")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-eddsa/#:~:text=Algorithms%20of%20this%20document%20MUST%20be%20enforced.", name="Specification")
    allure.dynamic.parent_suite("Data Integrity EdDSA Cryptosuites v1.0")
    allure.dynamic.suite("00 Introduction")
    allure.dynamic.sub_suite("00 Conformance")
    pytest.skip("TBD")

def test_conformance_2():
    allure.dynamic.title("02 Conforming processors MUST produce errors when non-conforming documents are consumed.")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-eddsa/#:~:text=Conforming%20processors%20MUST%20produce%20errors%20when%20non%2Dconforming%20documents%20are%20consumed.", name="Specification")
    allure.dynamic.parent_suite("Data Integrity EdDSA Cryptosuites v1.0")
    allure.dynamic.suite("00 Introduction")
    allure.dynamic.sub_suite("00 Conformance")
    pytest.skip("TBD")

def test_verification_methods_0():
    allure.dynamic.title("00 The publicKeyMultibase value of the verification method MUST start with the base-58-btc prefix (z), as defined in the Multibase section of Controller Documents 1.0")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-eddsa/#:~:text=The%20publicKeyMultibase%20value%20of%20the%20verification%20method%20MUST%20start%20with%20the%20base%2D58%2Dbtc%20prefix%20%28z%29%2C%20as%20defined%20in%20the%20Multibase%20section%20of%20Controller%20Documents%201.0", name="Specification")
    allure.dynamic.parent_suite("Data Integrity EdDSA Cryptosuites v1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("00 Verification methods")
    pytest.skip("TBD")

def test_verification_methods_1():
    allure.dynamic.title("01 A Multibase-encoded Multikey value follows, which MUST consist of a binary value that starts with the two-byte prefix 0xed01, which is the Multikey header for an Ed25519 public key, followed by the 32-byte public key data, all of which is then encoded using base-58-btc")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-eddsa/#:~:text=A%20Multibase%2Dencoded%20Multikey%20value%20follows%2C%20which%20MUST%20consist%20of%20a%20binary%20value%20that%20starts%20with%20the%20two%2Dbyte%20prefix%200xed01%2C%20which%20is%20the%20Multikey%20header%20for%20an%20Ed25519%20public%20key%2C%20followed%20by%20the%2032%2Dbyte%20public%20key%20data%2C%20all%20of%20which%20is%20then%20encoded%20using%20base%2D58%2Dbtc", name="Specification")
    allure.dynamic.parent_suite("Data Integrity EdDSA Cryptosuites v1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("00 Verification methods")
    pytest.skip("TBD")

def test_verification_methods_2():
    allure.dynamic.title("02 Any other encoding MUST NOT be allowed.")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-eddsa/#:~:text=Any%20other%20encoding%20MUST%20NOT%20be%20allowed.", name="Specification")
    allure.dynamic.parent_suite("Data Integrity EdDSA Cryptosuites v1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("00 Verification methods")
    pytest.skip("TBD")

def test_proof_representations_0():
    allure.dynamic.title("00 The type property MUST be DataIntegrityProof.")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-eddsa/#:~:text=The%20type%20property%20MUST%20be%20DataIntegrityProof.", name="Specification")
    allure.dynamic.parent_suite("Data Integrity EdDSA Cryptosuites v1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("01 Proof representations")
    pytest.skip("TBD")

def test_proof_representations_1():
    allure.dynamic.title("01 The cryptosuite property of the proof MUST be eddsa-rdfc-2022 or eddsa-jcs-2022.")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-eddsa/#:~:text=The%20cryptosuite%20property%20of%20the%20proof%20MUST%20be%20eddsa%2Drdfc%2D2022%20or%20eddsa%2Djcs%2D2022.", name="Specification")
    allure.dynamic.parent_suite("Data Integrity EdDSA Cryptosuites v1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("01 Proof representations")
    pytest.skip("TBD")

def test_proof_representations_2():
    allure.dynamic.title("02 The proofValue property of the proof MUST be a detached EdDSA signature produced according to [RFC8032], encoded using the base-58-btc header and alphabet as described in the Multibase section of Controller Documents 1.0.")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-eddsa/#:~:text=The%20proofValue%20property%20of%20the%20proof%20MUST%20be%20a%20detached%20EdDSA%20signature%20produced%20according%20to%20%5BRFC8032%5D%2C%20encoded%20using%20the%20base%2D58%2Dbtc%20header%20and%20alphabet%20as%20described%20in%20the%20Multibase%20section%20of%20Controller%20Documents%201.0.", name="Specification")
    allure.dynamic.parent_suite("Data Integrity EdDSA Cryptosuites v1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("01 Proof representations")
    pytest.skip("TBD")

def test_eddsa_rdfc_2022_0():
    allure.dynamic.title("00 The transformation options MUST contain a type identifier for the cryptographic suite (type) and a cryptosuite identifier (cryptosuite)")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-eddsa/#:~:text=The%20transformation%20options%20MUST%20contain%20a%20type%20identifier%20for%20the%20cryptographic%20suite%20%28type%29%20and%20a%20cryptosuite%20identifier%20%28cryptosuite%29", name="Specification")
    allure.dynamic.parent_suite("Data Integrity EdDSA Cryptosuites v1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("00 Eddsa rdfc 2022")
    pytest.skip("TBD")

def test_eddsa_rdfc_2022_1():
    allure.dynamic.title("01 Whenever this algorithm encodes strings, it MUST use UTF-8 encoding.")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-eddsa/#:~:text=Whenever%20this%20algorithm%20encodes%20strings%2C%20it%20MUST%20use%20UTF%2D8%20encoding.", name="Specification")
    allure.dynamic.parent_suite("Data Integrity EdDSA Cryptosuites v1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("00 Eddsa rdfc 2022")
    pytest.skip("TBD")

def test_eddsa_rdfc_2022_2():
    allure.dynamic.title("02 If options.type is not set to the string DataIntegrityProof and options.cryptosuite is not set to the string eddsa-rdfc-2022, an error MUST be raised that SHOULD convey an error type of PROOF_TRANSFORMATION_ERROR.")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-eddsa/#:~:text=If%20options.type%20is%20not%20set%20to%20the%20string%20DataIntegrityProof%20and%20options.cryptosuite%20is%20not%20set%20to%20the%20string%20eddsa%2Drdfc%2D2022%2C%20an%20error%20MUST%20be%20raised%20that%20SHOULD%20convey%20an%20error%20type%20of%20PROOF_TRANSFORMATION_ERROR.", name="Specification")
    allure.dynamic.parent_suite("Data Integrity EdDSA Cryptosuites v1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("00 Eddsa rdfc 2022")
    pytest.skip("TBD")

def test_eddsa_rdfc_2022_3():
    allure.dynamic.title("03 The proof options MUST contain a type identifier for the cryptographic suite (type) and MUST contain a cryptosuite identifier (cryptosuite)")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-eddsa/#:~:text=The%20proof%20options%20MUST%20contain%20a%20type%20identifier%20for%20the%20cryptographic%20suite%20%28type%29%20and%20MUST%20contain%20a%20cryptosuite%20identifier%20%28cryptosuite%29", name="Specification")
    allure.dynamic.parent_suite("Data Integrity EdDSA Cryptosuites v1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("00 Eddsa rdfc 2022")
    pytest.skip("TBD")

def test_eddsa_rdfc_2022_4():
    allure.dynamic.title("04 If proofConfig.type is not set to DataIntegrityProof and/or proofConfig.cryptosuite is not set to eddsa-rdfc-2022, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-eddsa/#:~:text=If%20proofConfig.type%20is%20not%20set%20to%20DataIntegrityProof%20and/or%20proofConfig.cryptosuite%20is%20not%20set%20to%20eddsa%2Drdfc%2D2022%2C%20an%20error%20MUST%20be%20raised%20and%20SHOULD%20convey%20an%20error%20type%20of%20PROOF_GENERATION_ERROR.", name="Specification")
    allure.dynamic.parent_suite("Data Integrity EdDSA Cryptosuites v1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("00 Eddsa rdfc 2022")
    pytest.skip("TBD")

def test_eddsa_rdfc_2022_5():
    allure.dynamic.title("05 If proofConfig.created is present and set to a value that is not a valid [XMLSCHEMA11-2] datetime, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-eddsa/#:~:text=If%20proofConfig.created%20is%20present%20and%20set%20to%20a%20value%20that%20is%20not%20a%20valid%20%5BXMLSCHEMA11%2D2%5D%20datetime%2C%20an%20error%20MUST%20be%20raised%20and%20SHOULD%20convey%20an%20error%20type%20of%20PROOF_GENERATION_ERROR.", name="Specification")
    allure.dynamic.parent_suite("Data Integrity EdDSA Cryptosuites v1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("00 Eddsa rdfc 2022")
    pytest.skip("TBD")

def test_eddsa_rdfc_2022_6():
    allure.dynamic.title("06 The proof options MUST contain a type identifier for the cryptographic suite (type) and MAY contain a cryptosuite identifier (cryptosuite)")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-eddsa/#:~:text=The%20proof%20options%20MUST%20contain%20a%20type%20identifier%20for%20the%20cryptographic%20suite%20%28type%29%20and%20MAY%20contain%20a%20cryptosuite%20identifier%20%28cryptosuite%29", name="Specification")
    allure.dynamic.parent_suite("Data Integrity EdDSA Cryptosuites v1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("00 Eddsa rdfc 2022")
    pytest.skip("TBD")

def test_eddsa_jcs_2022_0():
    allure.dynamic.title("00 The transformation options MUST contain a type identifier for the cryptographic suite (type) and a cryptosuite identifier (cryptosuite)")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-eddsa/#:~:text=The%20transformation%20options%20MUST%20contain%20a%20type%20identifier%20for%20the%20cryptographic%20suite%20%28type%29%20and%20a%20cryptosuite%20identifier%20%28cryptosuite%29", name="Specification")
    allure.dynamic.parent_suite("Data Integrity EdDSA Cryptosuites v1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("01 Eddsa jcs 2022")
    pytest.skip("TBD")

def test_eddsa_jcs_2022_1():
    allure.dynamic.title("01 Whenever this algorithm encodes strings, it MUST use UTF-8 encoding.")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-eddsa/#:~:text=Whenever%20this%20algorithm%20encodes%20strings%2C%20it%20MUST%20use%20UTF%2D8%20encoding.", name="Specification")
    allure.dynamic.parent_suite("Data Integrity EdDSA Cryptosuites v1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("01 Eddsa jcs 2022")
    pytest.skip("TBD")

def test_eddsa_jcs_2022_2():
    allure.dynamic.title("02 If options.type is not set to the string DataIntegrityProof and options.cryptosuite is not set to the string eddsa-jcs-2022, an error MUST be raised that SHOULD convey an error type of PROOF_VERIFICATION_ERROR.")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-eddsa/#:~:text=If%20options.type%20is%20not%20set%20to%20the%20string%20DataIntegrityProof%20and%20options.cryptosuite%20is%20not%20set%20to%20the%20string%20eddsa%2Djcs%2D2022%2C%20an%20error%20MUST%20be%20raised%20that%20SHOULD%20convey%20an%20error%20type%20of%20PROOF_VERIFICATION_ERROR.", name="Specification")
    allure.dynamic.parent_suite("Data Integrity EdDSA Cryptosuites v1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("01 Eddsa jcs 2022")
    pytest.skip("TBD")

def test_eddsa_jcs_2022_3():
    allure.dynamic.title("03 The proof options MUST contain a type identifier for the cryptographic suite (type) and MUST contain a cryptosuite identifier (cryptosuite)")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-eddsa/#:~:text=The%20proof%20options%20MUST%20contain%20a%20type%20identifier%20for%20the%20cryptographic%20suite%20%28type%29%20and%20MUST%20contain%20a%20cryptosuite%20identifier%20%28cryptosuite%29", name="Specification")
    allure.dynamic.parent_suite("Data Integrity EdDSA Cryptosuites v1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("01 Eddsa jcs 2022")
    pytest.skip("TBD")

def test_eddsa_jcs_2022_4():
    allure.dynamic.title("04 If proofConfig.type is not set to DataIntegrityProof or proofConfig.cryptosuite is not set to eddsa-jcs-2022, an error MUST be raised that SHOULD convey an error type of PROOF_GENERATION_ERROR.")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-eddsa/#:~:text=If%20proofConfig.type%20is%20not%20set%20to%20DataIntegrityProof%20or%20proofConfig.cryptosuite%20is%20not%20set%20to%20eddsa%2Djcs%2D2022%2C%20an%20error%20MUST%20be%20raised%20that%20SHOULD%20convey%20an%20error%20type%20of%20PROOF_GENERATION_ERROR.", name="Specification")
    allure.dynamic.parent_suite("Data Integrity EdDSA Cryptosuites v1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("01 Eddsa jcs 2022")
    pytest.skip("TBD")

def test_eddsa_jcs_2022_5():
    allure.dynamic.title("05 If proofConfig.created is set to a value that is not a valid [XMLSCHEMA11-2] datetime, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-eddsa/#:~:text=If%20proofConfig.created%20is%20set%20to%20a%20value%20that%20is%20not%20a%20valid%20%5BXMLSCHEMA11%2D2%5D%20datetime%2C%20an%20error%20MUST%20be%20raised%20and%20SHOULD%20convey%20an%20error%20type%20of%20PROOF_GENERATION_ERROR.", name="Specification")
    allure.dynamic.parent_suite("Data Integrity EdDSA Cryptosuites v1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("01 Eddsa jcs 2022")
    pytest.skip("TBD")

def test_eddsa_jcs_2022_6():
    allure.dynamic.title("06 The proof options MUST contain a type identifier for the cryptographic suite (type) and MAY contain a cryptosuite identifier (cryptosuite)")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-eddsa/#:~:text=The%20proof%20options%20MUST%20contain%20a%20type%20identifier%20for%20the%20cryptographic%20suite%20%28type%29%20and%20MAY%20contain%20a%20cryptosuite%20identifier%20%28cryptosuite%29", name="Specification")
    allure.dynamic.parent_suite("Data Integrity EdDSA Cryptosuites v1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("01 Eddsa jcs 2022")
    pytest.skip("TBD")

def test_data_model_0_0():
    allure.dynamic.title("00 The type of the verification method MUST be Ed25519VerificationKey2020.")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-eddsa/#:~:text=The%20type%20of%20the%20verification%20method%20MUST%20be%20Ed25519VerificationKey2020.", name="Specification")
    allure.dynamic.parent_suite("Data Integrity EdDSA Cryptosuites v1.0")
    allure.dynamic.suite("03 The ed25519signature2020 suite")
    allure.dynamic.sub_suite("00 Data model 0")
    pytest.skip("TBD")

def test_data_model_0_1():
    allure.dynamic.title("01 The controller of the verification method MUST be a URL.")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-eddsa/#:~:text=The%20controller%20of%20the%20verification%20method%20MUST%20be%20a%20URL.", name="Specification")
    allure.dynamic.parent_suite("Data Integrity EdDSA Cryptosuites v1.0")
    allure.dynamic.suite("03 The ed25519signature2020 suite")
    allure.dynamic.sub_suite("00 Data model 0")
    pytest.skip("TBD")

def test_data_model_0_2():
    allure.dynamic.title("02 The publicKeyMultibase value of the verification method MUST start with the base-58-btc prefix (z), as defined in the Multibase section of [VC-DATA-INTEGRITY]")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-eddsa/#:~:text=The%20publicKeyMultibase%20value%20of%20the%20verification%20method%20MUST%20start%20with%20the%20base%2D58%2Dbtc%20prefix%20%28z%29%2C%20as%20defined%20in%20the%20Multibase%20section%20of%20%5BVC%2DDATA%2DINTEGRITY%5D", name="Specification")
    allure.dynamic.parent_suite("Data Integrity EdDSA Cryptosuites v1.0")
    allure.dynamic.suite("03 The ed25519signature2020 suite")
    allure.dynamic.sub_suite("00 Data model 0")
    pytest.skip("TBD")

def test_data_model_0_3():
    allure.dynamic.title("03 A Multibase-encoded Multikey value follows, which MUST consist of a binary value that starts with the two-byte prefix 0xed01, which is the Multikey header for an Ed25519 public key, followed by the 32-byte public key data, all of which is then encoded using base-58-btc")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-eddsa/#:~:text=A%20Multibase%2Dencoded%20Multikey%20value%20follows%2C%20which%20MUST%20consist%20of%20a%20binary%20value%20that%20starts%20with%20the%20two%2Dbyte%20prefix%200xed01%2C%20which%20is%20the%20Multikey%20header%20for%20an%20Ed25519%20public%20key%2C%20followed%20by%20the%2032%2Dbyte%20public%20key%20data%2C%20all%20of%20which%20is%20then%20encoded%20using%20base%2D58%2Dbtc", name="Specification")
    allure.dynamic.parent_suite("Data Integrity EdDSA Cryptosuites v1.0")
    allure.dynamic.suite("03 The ed25519signature2020 suite")
    allure.dynamic.sub_suite("00 Data model 0")
    pytest.skip("TBD")

def test_data_model_0_4():
    allure.dynamic.title("04 Any other encoding MUST NOT be allowed.")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-eddsa/#:~:text=Any%20other%20encoding%20MUST%20NOT%20be%20allowed.", name="Specification")
    allure.dynamic.parent_suite("Data Integrity EdDSA Cryptosuites v1.0")
    allure.dynamic.suite("03 The ed25519signature2020 suite")
    allure.dynamic.sub_suite("00 Data model 0")
    pytest.skip("TBD")

def test_data_model_0_5():
    allure.dynamic.title("05 The verificationMethod property of the proof MUST be a URL")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-eddsa/#:~:text=The%20verificationMethod%20property%20of%20the%20proof%20MUST%20be%20a%20URL", name="Specification")
    allure.dynamic.parent_suite("Data Integrity EdDSA Cryptosuites v1.0")
    allure.dynamic.suite("03 The ed25519signature2020 suite")
    allure.dynamic.sub_suite("00 Data model 0")
    pytest.skip("TBD")

def test_data_model_0_6():
    allure.dynamic.title("06 Dereferencing the verificationMethod MUST result in an object containing a type property with the value set to Ed25519VerificationKey2020.")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-eddsa/#:~:text=Dereferencing%20the%20verificationMethod%20MUST%20result%20in%20an%20object%20containing%20a%20type%20property%20with%20the%20value%20set%20to%20Ed25519VerificationKey2020.", name="Specification")
    allure.dynamic.parent_suite("Data Integrity EdDSA Cryptosuites v1.0")
    allure.dynamic.suite("03 The ed25519signature2020 suite")
    allure.dynamic.sub_suite("00 Data model 0")
    pytest.skip("TBD")

def test_data_model_0_7():
    allure.dynamic.title("07 The type property of the proof MUST be Ed25519Signature2020.")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-eddsa/#:~:text=The%20type%20property%20of%20the%20proof%20MUST%20be%20Ed25519Signature2020.", name="Specification")
    allure.dynamic.parent_suite("Data Integrity EdDSA Cryptosuites v1.0")
    allure.dynamic.suite("03 The ed25519signature2020 suite")
    allure.dynamic.sub_suite("00 Data model 0")
    pytest.skip("TBD")

def test_data_model_0_8():
    allure.dynamic.title("08 The created property of the proof MUST be an [XMLSCHEMA11-2] formatted date string.")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-eddsa/#:~:text=The%20created%20property%20of%20the%20proof%20MUST%20be%20an%20%5BXMLSCHEMA11%2D2%5D%20formatted%20date%20string.", name="Specification")
    allure.dynamic.parent_suite("Data Integrity EdDSA Cryptosuites v1.0")
    allure.dynamic.suite("03 The ed25519signature2020 suite")
    allure.dynamic.sub_suite("00 Data model 0")
    pytest.skip("TBD")

def test_data_model_0_9():
    allure.dynamic.title("09 The proofPurpose property of the proof MUST be a string, and MUST match the verification relationship expressed by the verification method controller.")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-eddsa/#:~:text=The%20proofPurpose%20property%20of%20the%20proof%20MUST%20be%20a%20string%2C%20and%20MUST%20match%20the%20verification%20relationship%20expressed%20by%20the%20verification%20method%20controller.", name="Specification")
    allure.dynamic.parent_suite("Data Integrity EdDSA Cryptosuites v1.0")
    allure.dynamic.suite("03 The ed25519signature2020 suite")
    allure.dynamic.sub_suite("00 Data model 0")
    pytest.skip("TBD")

def test_data_model_0_10():
    allure.dynamic.title("10 The proofValue property of the proof MUST be a detached EdDSA produced according to [RFC8032], encoded using the base-58-btc header and alphabet as described in the Multibase section of [VC-DATA-INTEGRITY].")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-eddsa/#:~:text=The%20proofValue%20property%20of%20the%20proof%20MUST%20be%20a%20detached%20EdDSA%20produced%20according%20to%20%5BRFC8032%5D%2C%20encoded%20using%20the%20base%2D58%2Dbtc%20header%20and%20alphabet%20as%20described%20in%20the%20Multibase%20section%20of%20%5BVC%2DDATA%2DINTEGRITY%5D.", name="Specification")
    allure.dynamic.parent_suite("Data Integrity EdDSA Cryptosuites v1.0")
    allure.dynamic.suite("03 The ed25519signature2020 suite")
    allure.dynamic.sub_suite("00 Data model 0")
    pytest.skip("TBD")

def test_algorithms_0_0():
    allure.dynamic.title("00 To generate a proof, the algorithm in Section 4.1: Add Proof in the Data Integrity [VC-DATA-INTEGRITY] specification MUST be executed")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-eddsa/#:~:text=To%20generate%20a%20proof%2C%20the%20algorithm%20in%20Section%204.1%3A%20Add%20Proof%20in%20the%20Data%20Integrity%20%5BVC%2DDATA%2DINTEGRITY%5D%20specification%20MUST%20be%20executed", name="Specification")
    allure.dynamic.parent_suite("Data Integrity EdDSA Cryptosuites v1.0")
    allure.dynamic.suite("03 The ed25519signature2020 suite")
    allure.dynamic.sub_suite("01 Algorithms 0")
    pytest.skip("TBD")

def test_algorithms_0_1():
    allure.dynamic.title("01 To verify a proof, the algorithm in Section 4.2: Verify Proof in the Data Integrity [VC-DATA-INTEGRITY] specification MUST be executed")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-eddsa/#:~:text=To%20verify%20a%20proof%2C%20the%20algorithm%20in%20Section%204.2%3A%20Verify%20Proof%20in%20the%20Data%20Integrity%20%5BVC%2DDATA%2DINTEGRITY%5D%20specification%20MUST%20be%20executed", name="Specification")
    allure.dynamic.parent_suite("Data Integrity EdDSA Cryptosuites v1.0")
    allure.dynamic.suite("03 The ed25519signature2020 suite")
    allure.dynamic.sub_suite("01 Algorithms 0")
    pytest.skip("TBD")

def test_algorithms_0_2():
    allure.dynamic.title("02 The transformation options MUST contain a type identifier for the cryptographic suite (type) and a cryptosuite identifier (cryptosuite)")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-eddsa/#:~:text=The%20transformation%20options%20MUST%20contain%20a%20type%20identifier%20for%20the%20cryptographic%20suite%20%28type%29%20and%20a%20cryptosuite%20identifier%20%28cryptosuite%29", name="Specification")
    allure.dynamic.parent_suite("Data Integrity EdDSA Cryptosuites v1.0")
    allure.dynamic.suite("03 The ed25519signature2020 suite")
    allure.dynamic.sub_suite("01 Algorithms 0")
    pytest.skip("TBD")

def test_algorithms_0_3():
    allure.dynamic.title("03 Whenever this algorithm encodes strings, it MUST use UTF-8 encoding.")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-eddsa/#:~:text=Whenever%20this%20algorithm%20encodes%20strings%2C%20it%20MUST%20use%20UTF%2D8%20encoding.", name="Specification")
    allure.dynamic.parent_suite("Data Integrity EdDSA Cryptosuites v1.0")
    allure.dynamic.suite("03 The ed25519signature2020 suite")
    allure.dynamic.sub_suite("01 Algorithms 0")
    pytest.skip("TBD")

def test_algorithms_0_4():
    allure.dynamic.title("04 If options.type is not set to the string Ed25519Signature2020, an error MUST be raised that SHOULD convey an error type of PROOF_TRANSFORMATION_ERROR.")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-eddsa/#:~:text=If%20options.type%20is%20not%20set%20to%20the%20string%20Ed25519Signature2020%2C%20an%20error%20MUST%20be%20raised%20that%20SHOULD%20convey%20an%20error%20type%20of%20PROOF_TRANSFORMATION_ERROR.", name="Specification")
    allure.dynamic.parent_suite("Data Integrity EdDSA Cryptosuites v1.0")
    allure.dynamic.suite("03 The ed25519signature2020 suite")
    allure.dynamic.sub_suite("01 Algorithms 0")
    pytest.skip("TBD")

def test_algorithms_0_5():
    allure.dynamic.title("05 The proof configuration MUST contain a type identifier for the cryptographic suite (type) and MAY contain a cryptosuite identifier (cryptosuite)")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-eddsa/#:~:text=The%20proof%20configuration%20MUST%20contain%20a%20type%20identifier%20for%20the%20cryptographic%20suite%20%28type%29%20and%20MAY%20contain%20a%20cryptosuite%20identifier%20%28cryptosuite%29", name="Specification")
    allure.dynamic.parent_suite("Data Integrity EdDSA Cryptosuites v1.0")
    allure.dynamic.suite("03 The ed25519signature2020 suite")
    allure.dynamic.sub_suite("01 Algorithms 0")
    pytest.skip("TBD")

def test_algorithms_0_6():
    allure.dynamic.title("06 The proof options MUST contain a type identifier for the cryptographic suite (type) and MAY contain a cryptosuite identifier (cryptosuite)")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-eddsa/#:~:text=The%20proof%20options%20MUST%20contain%20a%20type%20identifier%20for%20the%20cryptographic%20suite%20%28type%29%20and%20MAY%20contain%20a%20cryptosuite%20identifier%20%28cryptosuite%29", name="Specification")
    allure.dynamic.parent_suite("Data Integrity EdDSA Cryptosuites v1.0")
    allure.dynamic.suite("03 The ed25519signature2020 suite")
    allure.dynamic.sub_suite("01 Algorithms 0")
    pytest.skip("TBD")

def test_algorithms_0_7():
    allure.dynamic.title("07 If proofConfig.type is not set to Ed25519Signature2020, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-eddsa/#:~:text=If%20proofConfig.type%20is%20not%20set%20to%20Ed25519Signature2020%2C%20an%20error%20MUST%20be%20raised%20and%20SHOULD%20convey%20an%20error%20type%20of%20PROOF_GENERATION_ERROR.", name="Specification")
    allure.dynamic.parent_suite("Data Integrity EdDSA Cryptosuites v1.0")
    allure.dynamic.suite("03 The ed25519signature2020 suite")
    allure.dynamic.sub_suite("01 Algorithms 0")
    pytest.skip("TBD")

def test_algorithms_0_8():
    allure.dynamic.title("08 If proofConfig.created is present and set to a value that is not a valid [XMLSCHEMA11-2] datetime, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-eddsa/#:~:text=If%20proofConfig.created%20is%20present%20and%20set%20to%20a%20value%20that%20is%20not%20a%20valid%20%5BXMLSCHEMA11%2D2%5D%20datetime%2C%20an%20error%20MUST%20be%20raised%20and%20SHOULD%20convey%20an%20error%20type%20of%20PROOF_GENERATION_ERROR.", name="Specification")
    allure.dynamic.parent_suite("Data Integrity EdDSA Cryptosuites v1.0")
    allure.dynamic.suite("03 The ed25519signature2020 suite")
    allure.dynamic.sub_suite("01 Algorithms 0")
    pytest.skip("TBD")
