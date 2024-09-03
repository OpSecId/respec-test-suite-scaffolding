import allure
import pytest

def test_conformance_0():
    allure.dynamic.title("00 The key words MAY, MUST, MUST NOT, and SHOULD in this document are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all capitals, as shown here.")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-ecdsa/#:~:text=The%20key%20words%20MAY%2C%20MUST%2C%20MUST%20NOT%2C%20and%20SHOULD%20in%20this%20document%20are%20to%20be%20interpreted%20as%20described%20in%20BCP%2014%20%5BRFC2119%5D%20%5BRFC8174%5D%20when%2C%20and%20only%20when%2C%20they%20appear%20in%20all%20capitals%2C%20as%20shown%20here.", name="Specification")
    allure.dynamic.parent_suite("Data Integrity ECDSA Cryptosuites v1.0")
    allure.dynamic.suite("00 Introduction")
    allure.dynamic.sub_suite("00 Conformance")
    pytest.skip("TBD")

def test_conformance_1():
    allure.dynamic.title("01 Algorithms of this document MUST be enforced.")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-ecdsa/#:~:text=Algorithms%20of%20this%20document%20MUST%20be%20enforced.", name="Specification")
    allure.dynamic.parent_suite("Data Integrity ECDSA Cryptosuites v1.0")
    allure.dynamic.suite("00 Introduction")
    allure.dynamic.sub_suite("00 Conformance")
    pytest.skip("TBD")

def test_conformance_2():
    allure.dynamic.title("02 Conforming processors MUST produce errors when non-conforming documents are consumed.")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-ecdsa/#:~:text=Conforming%20processors%20MUST%20produce%20errors%20when%20non%2Dconforming%20documents%20are%20consumed.", name="Specification")
    allure.dynamic.parent_suite("Data Integrity ECDSA Cryptosuites v1.0")
    allure.dynamic.suite("00 Introduction")
    allure.dynamic.sub_suite("00 Conformance")
    pytest.skip("TBD")

def test_verification_methods_0():
    allure.dynamic.title("00 The Multikey encoding of a P-256 public key MUST start with the two-byte prefix 0x8024 (the varint expression of 0x1200) followed by the 33-byte compressed public key data")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-ecdsa/#:~:text=The%20Multikey%20encoding%20of%20a%20P%2D256%20public%20key%20MUST%20start%20with%20the%20two%2Dbyte%20prefix%200x8024%20%28the%20varint%20expression%20of%200x1200%29%20followed%20by%20the%2033%2Dbyte%20compressed%20public%20key%20data", name="Specification")
    allure.dynamic.parent_suite("Data Integrity ECDSA Cryptosuites v1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("00 Verification methods")
    pytest.skip("TBD")

def test_verification_methods_1():
    allure.dynamic.title("01 The resulting 35-byte value MUST then be encoded using the base-58-btc alphabet, according to the Multibase section in the [controller-document] specification, and then prepended with the base-58-btc Multibase header (z).")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-ecdsa/#:~:text=The%20resulting%2035%2Dbyte%20value%20MUST%20then%20be%20encoded%20using%20the%20base%2D58%2Dbtc%20alphabet%2C%20according%20to%20the%20Multibase%20section%20in%20the%20%5Bcontroller%2Ddocument%5D%20specification%2C%20and%20then%20prepended%20with%20the%20base%2D58%2Dbtc%20Multibase%20header%20%28z%29.", name="Specification")
    allure.dynamic.parent_suite("Data Integrity ECDSA Cryptosuites v1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("00 Verification methods")
    pytest.skip("TBD")

def test_verification_methods_2():
    allure.dynamic.title("02 The encoding of a P-384 public key MUST start with the two-byte prefix 0x8124 (the varint expression of 0x1201) followed by the 49-byte compressed public key data")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-ecdsa/#:~:text=The%20encoding%20of%20a%20P%2D384%20public%20key%20MUST%20start%20with%20the%20two%2Dbyte%20prefix%200x8124%20%28the%20varint%20expression%20of%200x1201%29%20followed%20by%20the%2049%2Dbyte%20compressed%20public%20key%20data", name="Specification")
    allure.dynamic.parent_suite("Data Integrity ECDSA Cryptosuites v1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("00 Verification methods")
    pytest.skip("TBD")

def test_verification_methods_3():
    allure.dynamic.title("03 Any other encodings MUST NOT be allowed.")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-ecdsa/#:~:text=Any%20other%20encodings%20MUST%20NOT%20be%20allowed.", name="Specification")
    allure.dynamic.parent_suite("Data Integrity ECDSA Cryptosuites v1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("00 Verification methods")
    pytest.skip("TBD")

def test_verification_methods_4():
    allure.dynamic.title("04 The encoding of a P-256 secret key MUST start with the two-byte prefix 0x8626 (the varint expression of 0x1306) followed by the 32-byte secret key data")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-ecdsa/#:~:text=The%20encoding%20of%20a%20P%2D256%20secret%20key%20MUST%20start%20with%20the%20two%2Dbyte%20prefix%200x8626%20%28the%20varint%20expression%20of%200x1306%29%20followed%20by%20the%2032%2Dbyte%20secret%20key%20data", name="Specification")
    allure.dynamic.parent_suite("Data Integrity ECDSA Cryptosuites v1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("00 Verification methods")
    pytest.skip("TBD")

def test_verification_methods_5():
    allure.dynamic.title("05 The 34-byte value MUST then be encoded using the base-58-btc alphabet, according to the Multibase section in the [controller-document] specification, and then prepended with the base-58-btc Multibase header (z)")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-ecdsa/#:~:text=The%2034%2Dbyte%20value%20MUST%20then%20be%20encoded%20using%20the%20base%2D58%2Dbtc%20alphabet%2C%20according%20to%20the%20Multibase%20section%20in%20the%20%5Bcontroller%2Ddocument%5D%20specification%2C%20and%20then%20prepended%20with%20the%20base%2D58%2Dbtc%20Multibase%20header%20%28z%29", name="Specification")
    allure.dynamic.parent_suite("Data Integrity ECDSA Cryptosuites v1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("00 Verification methods")
    pytest.skip("TBD")

def test_verification_methods_6():
    allure.dynamic.title("06 The 50-byte value MUST then be encoded using the base-58-btc alphabet, according to the Multibase section in the [controller-document] specification, and then prepended with the base-58-btc Multibase header (z)")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-ecdsa/#:~:text=The%2050%2Dbyte%20value%20MUST%20then%20be%20encoded%20using%20the%20base%2D58%2Dbtc%20alphabet%2C%20according%20to%20the%20Multibase%20section%20in%20the%20%5Bcontroller%2Ddocument%5D%20specification%2C%20and%20then%20prepended%20with%20the%20base%2D58%2Dbtc%20Multibase%20header%20%28z%29", name="Specification")
    allure.dynamic.parent_suite("Data Integrity ECDSA Cryptosuites v1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("00 Verification methods")
    pytest.skip("TBD")

def test_proof_representations_0():
    allure.dynamic.title("00 The type property MUST be DataIntegrityProof.")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-ecdsa/#:~:text=The%20type%20property%20MUST%20be%20DataIntegrityProof.", name="Specification")
    allure.dynamic.parent_suite("Data Integrity ECDSA Cryptosuites v1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("01 Proof representations")
    pytest.skip("TBD")

def test_proof_representations_1():
    allure.dynamic.title("01 The cryptosuite property MUST be ecdsa-rdfc-2019, ecdsa-jcs-2019, or ecdsa-sd-2023.")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-ecdsa/#:~:text=The%20cryptosuite%20property%20MUST%20be%20ecdsa%2Drdfc%2D2019%2C%20ecdsa%2Djcs%2D2019%2C%20or%20ecdsa%2Dsd%2D2023.", name="Specification")
    allure.dynamic.parent_suite("Data Integrity ECDSA Cryptosuites v1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("01 Proof representations")
    pytest.skip("TBD")

def test_ecdsa_rdfc_2019_0():
    allure.dynamic.title("00 The transformation options MUST contain a type identifier for the cryptographic suite (type) and a cryptosuite identifier (cryptosuite)")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-ecdsa/#:~:text=The%20transformation%20options%20MUST%20contain%20a%20type%20identifier%20for%20the%20cryptographic%20suite%20%28type%29%20and%20a%20cryptosuite%20identifier%20%28cryptosuite%29", name="Specification")
    allure.dynamic.parent_suite("Data Integrity ECDSA Cryptosuites v1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("00 Ecdsa rdfc 2019")
    pytest.skip("TBD")

def test_ecdsa_rdfc_2019_1():
    allure.dynamic.title("01 Whenever this algorithm encodes strings, it MUST use UTF-8 encoding.")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-ecdsa/#:~:text=Whenever%20this%20algorithm%20encodes%20strings%2C%20it%20MUST%20use%20UTF%2D8%20encoding.", name="Specification")
    allure.dynamic.parent_suite("Data Integrity ECDSA Cryptosuites v1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("00 Ecdsa rdfc 2019")
    pytest.skip("TBD")

def test_ecdsa_rdfc_2019_2():
    allure.dynamic.title("02 If options.type is not set to the string DataIntegrityProof and options.cryptosuite is not set to the string ecdsa-rdfc-2019, an error MUST be raised and SHOULD convey an error type of PROOF_TRANSFORMATION_ERROR.")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-ecdsa/#:~:text=If%20options.type%20is%20not%20set%20to%20the%20string%20DataIntegrityProof%20and%20options.cryptosuite%20is%20not%20set%20to%20the%20string%20ecdsa%2Drdfc%2D2019%2C%20an%20error%20MUST%20be%20raised%20and%20SHOULD%20convey%20an%20error%20type%20of%20PROOF_TRANSFORMATION_ERROR.", name="Specification")
    allure.dynamic.parent_suite("Data Integrity ECDSA Cryptosuites v1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("00 Ecdsa rdfc 2019")
    pytest.skip("TBD")

def test_ecdsa_rdfc_2019_3():
    allure.dynamic.title("03 The proof options MUST contain a type identifier for the cryptographic suite (type) and MUST contain a cryptosuite identifier (cryptosuite)")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-ecdsa/#:~:text=The%20proof%20options%20MUST%20contain%20a%20type%20identifier%20for%20the%20cryptographic%20suite%20%28type%29%20and%20MUST%20contain%20a%20cryptosuite%20identifier%20%28cryptosuite%29", name="Specification")
    allure.dynamic.parent_suite("Data Integrity ECDSA Cryptosuites v1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("00 Ecdsa rdfc 2019")
    pytest.skip("TBD")

def test_ecdsa_rdfc_2019_4():
    allure.dynamic.title("04 If proofConfig.type is not set to DataIntegrityProof and/or proofConfig.cryptosuite is not set to ecdsa-rdfc-2019, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-ecdsa/#:~:text=If%20proofConfig.type%20is%20not%20set%20to%20DataIntegrityProof%20and/or%20proofConfig.cryptosuite%20is%20not%20set%20to%20ecdsa%2Drdfc%2D2019%2C%20an%20error%20MUST%20be%20raised%20and%20SHOULD%20convey%20an%20error%20type%20of%20PROOF_GENERATION_ERROR.", name="Specification")
    allure.dynamic.parent_suite("Data Integrity ECDSA Cryptosuites v1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("00 Ecdsa rdfc 2019")
    pytest.skip("TBD")

def test_ecdsa_rdfc_2019_5():
    allure.dynamic.title("05 If proofConfig.created is set and if the value is not a valid [XMLSCHEMA11-2] datetime, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-ecdsa/#:~:text=If%20proofConfig.created%20is%20set%20and%20if%20the%20value%20is%20not%20a%20valid%20%5BXMLSCHEMA11%2D2%5D%20datetime%2C%20an%20error%20MUST%20be%20raised%20and%20SHOULD%20convey%20an%20error%20type%20of%20PROOF_GENERATION_ERROR.", name="Specification")
    allure.dynamic.parent_suite("Data Integrity ECDSA Cryptosuites v1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("00 Ecdsa rdfc 2019")
    pytest.skip("TBD")

def test_ecdsa_rdfc_2019_6():
    allure.dynamic.title("06 The proof options MUST contain a type identifier for the cryptographic suite (type) and MAY contain a cryptosuite identifier (cryptosuite)")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-ecdsa/#:~:text=The%20proof%20options%20MUST%20contain%20a%20type%20identifier%20for%20the%20cryptographic%20suite%20%28type%29%20and%20MAY%20contain%20a%20cryptosuite%20identifier%20%28cryptosuite%29", name="Specification")
    allure.dynamic.parent_suite("Data Integrity ECDSA Cryptosuites v1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("00 Ecdsa rdfc 2019")
    pytest.skip("TBD")

def test_ecdsa_jcs_2019_0():
    allure.dynamic.title("00 The transformation options MUST contain a type identifier for the cryptographic suite (type) and a cryptosuite identifier (cryptosuite)")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-ecdsa/#:~:text=The%20transformation%20options%20MUST%20contain%20a%20type%20identifier%20for%20the%20cryptographic%20suite%20%28type%29%20and%20a%20cryptosuite%20identifier%20%28cryptosuite%29", name="Specification")
    allure.dynamic.parent_suite("Data Integrity ECDSA Cryptosuites v1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("01 Ecdsa jcs 2019")
    pytest.skip("TBD")

def test_ecdsa_jcs_2019_1():
    allure.dynamic.title("01 Whenever this algorithm encodes strings, it MUST use UTF-8 encoding.")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-ecdsa/#:~:text=Whenever%20this%20algorithm%20encodes%20strings%2C%20it%20MUST%20use%20UTF%2D8%20encoding.", name="Specification")
    allure.dynamic.parent_suite("Data Integrity ECDSA Cryptosuites v1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("01 Ecdsa jcs 2019")
    pytest.skip("TBD")

def test_ecdsa_jcs_2019_2():
    allure.dynamic.title("02 If options.type is not set to the string DataIntegrityProof or options.cryptosuite is not set to the string ecdsa-jcs-2019, an error MUST be raised and SHOULD convey an error type of PROOF_TRANSFORMATION_ERROR.")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-ecdsa/#:~:text=If%20options.type%20is%20not%20set%20to%20the%20string%20DataIntegrityProof%20or%20options.cryptosuite%20is%20not%20set%20to%20the%20string%20ecdsa%2Djcs%2D2019%2C%20an%20error%20MUST%20be%20raised%20and%20SHOULD%20convey%20an%20error%20type%20of%20PROOF_TRANSFORMATION_ERROR.", name="Specification")
    allure.dynamic.parent_suite("Data Integrity ECDSA Cryptosuites v1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("01 Ecdsa jcs 2019")
    pytest.skip("TBD")

def test_ecdsa_jcs_2019_3():
    allure.dynamic.title("03 The proof options MUST contain a type identifier for the cryptographic suite (type) and MUST contain a cryptosuite identifier (cryptosuite)")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-ecdsa/#:~:text=The%20proof%20options%20MUST%20contain%20a%20type%20identifier%20for%20the%20cryptographic%20suite%20%28type%29%20and%20MUST%20contain%20a%20cryptosuite%20identifier%20%28cryptosuite%29", name="Specification")
    allure.dynamic.parent_suite("Data Integrity ECDSA Cryptosuites v1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("01 Ecdsa jcs 2019")
    pytest.skip("TBD")

def test_ecdsa_jcs_2019_4():
    allure.dynamic.title("04 If proofConfig.type is not set to DataIntegrityProof and/or proofConfig.cryptosuite is not set to ecdsa-jcs-2019, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-ecdsa/#:~:text=If%20proofConfig.type%20is%20not%20set%20to%20DataIntegrityProof%20and/or%20proofConfig.cryptosuite%20is%20not%20set%20to%20ecdsa%2Djcs%2D2019%2C%20an%20error%20MUST%20be%20raised%20and%20SHOULD%20convey%20an%20error%20type%20of%20PROOF_GENERATION_ERROR.", name="Specification")
    allure.dynamic.parent_suite("Data Integrity ECDSA Cryptosuites v1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("01 Ecdsa jcs 2019")
    pytest.skip("TBD")

def test_ecdsa_jcs_2019_5():
    allure.dynamic.title("05 If proofConfig.created is set and if the value is not a valid [XMLSCHEMA11-2] datetime, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-ecdsa/#:~:text=If%20proofConfig.created%20is%20set%20and%20if%20the%20value%20is%20not%20a%20valid%20%5BXMLSCHEMA11%2D2%5D%20datetime%2C%20an%20error%20MUST%20be%20raised%20and%20SHOULD%20convey%20an%20error%20type%20of%20PROOF_GENERATION_ERROR.", name="Specification")
    allure.dynamic.parent_suite("Data Integrity ECDSA Cryptosuites v1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("01 Ecdsa jcs 2019")
    pytest.skip("TBD")

def test_ecdsa_jcs_2019_6():
    allure.dynamic.title("06 The proof options MUST contain a type identifier for the cryptographic suite (type) and MAY contain a cryptosuite identifier (cryptosuite)")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-ecdsa/#:~:text=The%20proof%20options%20MUST%20contain%20a%20type%20identifier%20for%20the%20cryptographic%20suite%20%28type%29%20and%20MAY%20contain%20a%20cryptosuite%20identifier%20%28cryptosuite%29", name="Specification")
    allure.dynamic.parent_suite("Data Integrity ECDSA Cryptosuites v1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("01 Ecdsa jcs 2019")
    pytest.skip("TBD")

def test_selective_disclosure_functions_0():
    allure.dynamic.title("00 Note: All non-blank node identifiers in the path of any JSON Pointer MUST be included in the selection, this includes any root document identifier.")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-ecdsa/#:~:text=Note%3A%20All%20non%2Dblank%20node%20identifiers%20in%20the%20path%20of%20any%20JSON%20Pointer%20MUST%20be%20included%20in%20the%20selection%2C%20this%20includes%20any%20root%20document%20identifier.", name="Specification")
    allure.dynamic.parent_suite("Data Integrity ECDSA Cryptosuites v1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("02 Selective disclosure functions")
    pytest.skip("TBD")

def test_selective_disclosure_functions_1():
    allure.dynamic.title("01 Note: The selection MUST include all types in the path of any JSON Pointer, including any root document type.")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-ecdsa/#:~:text=Note%3A%20The%20selection%20MUST%20include%20all%20types%20in%20the%20path%20of%20any%20JSON%20Pointer%2C%20including%20any%20root%20document%20type.", name="Specification")
    allure.dynamic.parent_suite("Data Integrity ECDSA Cryptosuites v1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("02 Selective disclosure functions")
    pytest.skip("TBD")

def test_selective_disclosure_functions_2():
    allure.dynamic.title("02 If value is now undefined, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR, indicating that the JSON pointer does not match the given document.")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-ecdsa/#:~:text=If%20value%20is%20now%20undefined%2C%20an%20error%20MUST%20be%20raised%20and%20SHOULD%20convey%20an%20error%20type%20of%20PROOF_GENERATION_ERROR%2C%20indicating%20that%20the%20JSON%20pointer%20does%20not%20match%20the%20given%20document.", name="Specification")
    allure.dynamic.parent_suite("Data Integrity ECDSA Cryptosuites v1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("02 Selective disclosure functions")
    pytest.skip("TBD")

def test_ecdsa_sd_2023_functions_0():
    allure.dynamic.title("00 CBOR-encode components per [RFC8949] where CBOR tagging MUST NOT be used on any of the components")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-ecdsa/#:~:text=CBOR%2Dencode%20components%20per%20%5BRFC8949%5D%20where%20CBOR%20tagging%20MUST%20NOT%20be%20used%20on%20any%20of%20the%20components", name="Specification")
    allure.dynamic.parent_suite("Data Integrity ECDSA Cryptosuites v1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("03 Ecdsa sd 2023 functions")
    pytest.skip("TBD")

def test_ecdsa_sd_2023_functions_1():
    allure.dynamic.title("01 If the proofValue string does not start with u, indicating that it is a multibase-base64url-no-pad-encoded value, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-ecdsa/#:~:text=If%20the%20proofValue%20string%20does%20not%20start%20with%20u%2C%20indicating%20that%20it%20is%20a%20multibase%2Dbase64url%2Dno%2Dpad%2Dencoded%20value%2C%20an%20error%20MUST%20be%20raised%20and%20SHOULD%20convey%20an%20error%20type%20of%20PROOF_VERIFICATION_ERROR.", name="Specification")
    allure.dynamic.parent_suite("Data Integrity ECDSA Cryptosuites v1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("03 Ecdsa sd 2023 functions")
    pytest.skip("TBD")

def test_ecdsa_sd_2023_functions_2():
    allure.dynamic.title("02 If the decodedProofValue does not start with the ECDSA-SD base proof header bytes 0xd9, 0x5d, and 0x00, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-ecdsa/#:~:text=If%20the%20decodedProofValue%20does%20not%20start%20with%20the%20ECDSA%2DSD%20base%20proof%20header%20bytes%200xd9%2C%200x5d%2C%20and%200x00%2C%20an%20error%20MUST%20be%20raised%20and%20SHOULD%20convey%20an%20error%20type%20of%20PROOF_VERIFICATION_ERROR.", name="Specification")
    allure.dynamic.parent_suite("Data Integrity ECDSA Cryptosuites v1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("03 Ecdsa sd 2023 functions")
    pytest.skip("TBD")

def test_ecdsa_sd_2023_functions_3():
    allure.dynamic.title("03 If the decodedProofValue does not start with the ECDSA-SD disclosure proof header bytes 0xd9, 0x5d, and 0x01, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-ecdsa/#:~:text=If%20the%20decodedProofValue%20does%20not%20start%20with%20the%20ECDSA%2DSD%20disclosure%20proof%20header%20bytes%200xd9%2C%200x5d%2C%20and%200x01%2C%20an%20error%20MUST%20be%20raised%20and%20SHOULD%20convey%20an%20error%20type%20of%20PROOF_VERIFICATION_ERROR.", name="Specification")
    allure.dynamic.parent_suite("Data Integrity ECDSA Cryptosuites v1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("03 Ecdsa sd 2023 functions")
    pytest.skip("TBD")

def test_ecdsa_sd_2023_functions_4():
    allure.dynamic.title("04 If the result is not an array of the following five elements — a byte array of length 64; a byte array of length 36; an array of byte arrays, each of length 64; a map of integers to byte arrays, each of length 32; and an array of integers — an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-ecdsa/#:~:text=If%20the%20result%20is%20not%20an%20array%20of%20the%20following%20five%20elements%20%E2%80%94%20a%20byte%20array%20of%20length%2064%3B%20a%20byte%20array%20of%20length%2036%3B%20an%20array%20of%20byte%20arrays%2C%20each%20of%20length%2064%3B%20a%20map%20of%20integers%20to%20byte%20arrays%2C%20each%20of%20length%2032%3B%20and%20an%20array%20of%20integers%20%E2%80%94%20an%20error%20MUST%20be%20raised%20and%20SHOULD%20convey%20an%20error%20type%20of%20PROOF_VERIFICATION_ERROR.", name="Specification")
    allure.dynamic.parent_suite("Data Integrity ECDSA Cryptosuites v1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("03 Ecdsa sd 2023 functions")
    pytest.skip("TBD")

def test_ecdsa_sd_2023_0():
    allure.dynamic.title("00 The transformation options MUST contain a type identifier for the cryptographic suite (type), a cryptosuite identifier (cryptosuite), and a verification method (verificationMethod)")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-ecdsa/#:~:text=The%20transformation%20options%20MUST%20contain%20a%20type%20identifier%20for%20the%20cryptographic%20suite%20%28type%29%2C%20a%20cryptosuite%20identifier%20%28cryptosuite%29%2C%20and%20a%20verification%20method%20%28verificationMethod%29", name="Specification")
    allure.dynamic.parent_suite("Data Integrity ECDSA Cryptosuites v1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("04 Ecdsa sd 2023")
    pytest.skip("TBD")

def test_ecdsa_sd_2023_1():
    allure.dynamic.title("01 The transformation options MUST contain an array of mandatory JSON pointers (mandatoryPointers) and MAY contain additional options, such as a JSON-LD document loader")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-ecdsa/#:~:text=The%20transformation%20options%20MUST%20contain%20an%20array%20of%20mandatory%20JSON%20pointers%20%28mandatoryPointers%29%20and%20MAY%20contain%20additional%20options%2C%20such%20as%20a%20JSON%2DLD%20document%20loader", name="Specification")
    allure.dynamic.parent_suite("Data Integrity ECDSA Cryptosuites v1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("04 Ecdsa sd 2023")
    pytest.skip("TBD")

def test_ecdsa_sd_2023_2():
    allure.dynamic.title("02 Whenever this algorithm encodes strings, it MUST use UTF-8 encoding.")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-ecdsa/#:~:text=Whenever%20this%20algorithm%20encodes%20strings%2C%20it%20MUST%20use%20UTF%2D8%20encoding.", name="Specification")
    allure.dynamic.parent_suite("Data Integrity ECDSA Cryptosuites v1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("04 Ecdsa sd 2023")
    pytest.skip("TBD")

def test_ecdsa_sd_2023_3():
    allure.dynamic.title("03 Per the recommendations of [RFC2104], the HMAC key MUST be the same length as the digest size; for SHA-256, this is 256 bits or 32 bytes.")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-ecdsa/#:~:text=Per%20the%20recommendations%20of%20%5BRFC2104%5D%2C%20the%20HMAC%20key%20MUST%20be%20the%20same%20length%20as%20the%20digest%20size%3B%20for%20SHA%2D256%2C%20this%20is%20256%20bits%20or%2032%20bytes.", name="Specification")
    allure.dynamic.parent_suite("Data Integrity ECDSA Cryptosuites v1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("04 Ecdsa sd 2023")
    pytest.skip("TBD")

def test_ecdsa_sd_2023_4():
    allure.dynamic.title("04 The proof options MUST contain a type identifier for the cryptographic suite (type) and MUST contain a cryptosuite identifier (cryptosuite)")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-ecdsa/#:~:text=The%20proof%20options%20MUST%20contain%20a%20type%20identifier%20for%20the%20cryptographic%20suite%20%28type%29%20and%20MUST%20contain%20a%20cryptosuite%20identifier%20%28cryptosuite%29", name="Specification")
    allure.dynamic.parent_suite("Data Integrity ECDSA Cryptosuites v1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("04 Ecdsa sd 2023")
    pytest.skip("TBD")

def test_ecdsa_sd_2023_5():
    allure.dynamic.title("05 If proofConfig.type is not set to DataIntegrityProof and/or proofConfig.cryptosuite is not set to ecdsa-sd-2023, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-ecdsa/#:~:text=If%20proofConfig.type%20is%20not%20set%20to%20DataIntegrityProof%20and/or%20proofConfig.cryptosuite%20is%20not%20set%20to%20ecdsa%2Dsd%2D2023%2C%20an%20error%20MUST%20be%20raised%20and%20SHOULD%20convey%20an%20error%20type%20of%20PROOF_GENERATION_ERROR.", name="Specification")
    allure.dynamic.parent_suite("Data Integrity ECDSA Cryptosuites v1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("04 Ecdsa sd 2023")
    pytest.skip("TBD")

def test_ecdsa_sd_2023_6():
    allure.dynamic.title("06 If proofConfig.created is set and if the value is not a valid [XMLSCHEMA11-2] datetime, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-ecdsa/#:~:text=If%20proofConfig.created%20is%20set%20and%20if%20the%20value%20is%20not%20a%20valid%20%5BXMLSCHEMA11%2D2%5D%20datetime%2C%20an%20error%20MUST%20be%20raised%20and%20SHOULD%20convey%20an%20error%20type%20of%20PROOF_GENERATION_ERROR.", name="Specification")
    allure.dynamic.parent_suite("Data Integrity ECDSA Cryptosuites v1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("04 Ecdsa sd 2023")
    pytest.skip("TBD")

def test_ecdsa_sd_2023_7():
    allure.dynamic.title("07 The proof options MUST contain a type identifier for the cryptographic suite (type) and MAY contain a cryptosuite identifier (cryptosuite)")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-ecdsa/#:~:text=The%20proof%20options%20MUST%20contain%20a%20type%20identifier%20for%20the%20cryptographic%20suite%20%28type%29%20and%20MAY%20contain%20a%20cryptosuite%20identifier%20%28cryptosuite%29", name="Specification")
    allure.dynamic.parent_suite("Data Integrity ECDSA Cryptosuites v1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("04 Ecdsa sd 2023")
    pytest.skip("TBD")

def test_ecdsa_sd_2023_8():
    allure.dynamic.title("08 If the length of signatures does not match the length of nonMandatory, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR, indicating that the signature count does not match the non-mandatory message count.")
    allure.dynamic.link("https://www.w3.org/TR/vc-di-ecdsa/#:~:text=If%20the%20length%20of%20signatures%20does%20not%20match%20the%20length%20of%20nonMandatory%2C%20an%20error%20MUST%20be%20raised%20and%20SHOULD%20convey%20an%20error%20type%20of%20PROOF_VERIFICATION_ERROR%2C%20indicating%20that%20the%20signature%20count%20does%20not%20match%20the%20non%2Dmandatory%20message%20count.", name="Specification")
    allure.dynamic.parent_suite("Data Integrity ECDSA Cryptosuites v1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("04 Ecdsa sd 2023")
    pytest.skip("TBD")
