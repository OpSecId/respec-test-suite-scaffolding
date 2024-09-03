import allure
import pytest

def test_conformance_0():
    allure.dynamic.title("00 The key words MAY, MUST, MUST NOT, SHOULD, and SHOULD NOT in this document are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all capitals, as shown here.")
    allure.dynamic.link("https://www.w3.org/TR/vc-bitstring-status-list/#:~:text=The%20key%20words%20MAY%2C%20MUST%2C%20MUST%20NOT%2C%20SHOULD%2C%20and%20SHOULD%20NOT%20in%20this%20document%20are%20to%20be%20interpreted%20as%20described%20in%20BCP%2014%20%5BRFC2119%5D%20%5BRFC8174%5D%20when%2C%20and%20only%20when%2C%20they%20appear%20in%20all%20capitals%2C%20as%20shown%20here.", name="Specification")
    allure.dynamic.parent_suite("Bitstring Status List v1.0")
    allure.dynamic.suite("00 Introduction")
    allure.dynamic.sub_suite("00 Conformance")
    pytest.skip("TBD")

def test_conformance_1():
    allure.dynamic.title("01 Conforming processors MUST produce errors when non-conforming documents are consumed.")
    allure.dynamic.link("https://www.w3.org/TR/vc-bitstring-status-list/#:~:text=Conforming%20processors%20MUST%20produce%20errors%20when%20non%2Dconforming%20documents%20are%20consumed.", name="Specification")
    allure.dynamic.parent_suite("Bitstring Status List v1.0")
    allure.dynamic.suite("00 Introduction")
    allure.dynamic.sub_suite("00 Conformance")
    pytest.skip("TBD")

def test_bitstringstatuslistentry_0():
    allure.dynamic.title("00 Any expression of the data model in this section MUST be expressed in a conforming verifiable credential as defined in [VC-DATA-MODEL-2.0].")
    allure.dynamic.link("https://www.w3.org/TR/vc-bitstring-status-list/#:~:text=Any%20expression%20of%20the%20data%20model%20in%20this%20section%20MUST%20be%20expressed%20in%20a%20conforming%20verifiable%20credential%20as%20defined%20in%20%5BVC%2DDATA%2DMODEL%2D2.0%5D.", name="Specification")
    allure.dynamic.parent_suite("Bitstring Status List v1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("00 Bitstringstatuslistentry")
    pytest.skip("TBD")

def test_bitstringstatuslistentry_1():
    allure.dynamic.title("01 It MUST NOT be the URL for the status list")
    allure.dynamic.link("https://www.w3.org/TR/vc-bitstring-status-list/#:~:text=It%20MUST%20NOT%20be%20the%20URL%20for%20the%20status%20list", name="Specification")
    allure.dynamic.parent_suite("Bitstring Status List v1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("00 Bitstringstatuslistentry")
    pytest.skip("TBD")

def test_bitstringstatuslistentry_2():
    allure.dynamic.title("02 The type property MUST be BitstringStatusListEntry.")
    allure.dynamic.link("https://www.w3.org/TR/vc-bitstring-status-list/#:~:text=The%20type%20property%20MUST%20be%20BitstringStatusListEntry.", name="Specification")
    allure.dynamic.parent_suite("Bitstring Status List v1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("00 Bitstringstatuslistentry")
    pytest.skip("TBD")

def test_bitstringstatuslistentry_3():
    allure.dynamic.title("03 The purpose of the status entry MUST be a string")
    allure.dynamic.link("https://www.w3.org/TR/vc-bitstring-status-list/#:~:text=The%20purpose%20of%20the%20status%20entry%20MUST%20be%20a%20string", name="Specification")
    allure.dynamic.parent_suite("Bitstring Status List v1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("00 Bitstringstatuslistentry")
    pytest.skip("TBD")

def test_bitstringstatuslistentry_4():
    allure.dynamic.title("04 While the value of the string is arbitrary, the following values MUST be used for their intended purpose: Value Description revocation Used to cancel the validity of a verifiable credential")
    allure.dynamic.link("https://www.w3.org/TR/vc-bitstring-status-list/#:~:text=While%20the%20value%20of%20the%20string%20is%20arbitrary%2C%20the%20following%20values%20MUST%20be%20used%20for%20their%20intended%20purpose%3A%20Value%20Description%20revocation%20Used%20to%20cancel%20the%20validity%20of%20a%20verifiable%20credential", name="Specification")
    allure.dynamic.parent_suite("Bitstring Status List v1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("00 Bitstringstatuslistentry")
    pytest.skip("TBD")

def test_bitstringstatuslistentry_5():
    allure.dynamic.title("05 The statusListIndex property MUST be an arbitrary size integer greater than or equal to 0, expressed as a string in base 10")
    allure.dynamic.link("https://www.w3.org/TR/vc-bitstring-status-list/#:~:text=The%20statusListIndex%20property%20MUST%20be%20an%20arbitrary%20size%20integer%20greater%20than%20or%20equal%20to%200%2C%20expressed%20as%20a%20string%20in%20base%2010", name="Specification")
    allure.dynamic.parent_suite("Bitstring Status List v1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("00 Bitstringstatuslistentry")
    pytest.skip("TBD")

def test_bitstringstatuslistentry_6():
    allure.dynamic.title("06 The statusListCredential property MUST be a URL to a verifiable credential")
    allure.dynamic.link("https://www.w3.org/TR/vc-bitstring-status-list/#:~:text=The%20statusListCredential%20property%20MUST%20be%20a%20URL%20to%20a%20verifiable%20credential", name="Specification")
    allure.dynamic.parent_suite("Bitstring Status List v1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("00 Bitstringstatuslistentry")
    pytest.skip("TBD")

def test_bitstringstatuslistentry_7():
    allure.dynamic.title("07 When the URL is dereferenced, the resulting verifiable credential MUST have type property that includes the BitstringStatusListCredential value.")
    allure.dynamic.link("https://www.w3.org/TR/vc-bitstring-status-list/#:~:text=When%20the%20URL%20is%20dereferenced%2C%20the%20resulting%20verifiable%20credential%20MUST%20have%20type%20property%20that%20includes%20the%20BitstringStatusListCredential%20value.", name="Specification")
    allure.dynamic.parent_suite("Bitstring Status List v1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("00 Bitstringstatuslistentry")
    pytest.skip("TBD")

def test_bitstringstatuslistentry_8():
    allure.dynamic.title("08 If statusSize is not present as a property of the credentialStatus, then statusSize MUST be processed as 1")
    allure.dynamic.link("https://www.w3.org/TR/vc-bitstring-status-list/#:~:text=If%20statusSize%20is%20not%20present%20as%20a%20property%20of%20the%20credentialStatus%2C%20then%20statusSize%20MUST%20be%20processed%20as%201", name="Specification")
    allure.dynamic.parent_suite("Bitstring Status List v1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("00 Bitstringstatuslistentry")
    pytest.skip("TBD")

def test_bitstringstatuslistentry_9():
    allure.dynamic.title("09 If present, statusSize MUST be an integer greater than zero")
    allure.dynamic.link("https://www.w3.org/TR/vc-bitstring-status-list/#:~:text=If%20present%2C%20statusSize%20MUST%20be%20an%20integer%20greater%20than%20zero", name="Specification")
    allure.dynamic.parent_suite("Bitstring Status List v1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("00 Bitstringstatuslistentry")
    pytest.skip("TBD")

def test_bitstringstatuslistentry_10():
    allure.dynamic.title("10 If statusSize is provided and is greater than 1, then the property credentialStatus.statusMessage MUST be present, and the number of status messages MUST equal the number of possible values.")
    allure.dynamic.link("https://www.w3.org/TR/vc-bitstring-status-list/#:~:text=If%20statusSize%20is%20provided%20and%20is%20greater%20than%201%2C%20then%20the%20property%20credentialStatus.statusMessage%20MUST%20be%20present%2C%20and%20the%20number%20of%20status%20messages%20MUST%20equal%20the%20number%20of%20possible%20values.", name="Specification")
    allure.dynamic.parent_suite("Bitstring Status List v1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("00 Bitstringstatuslistentry")
    pytest.skip("TBD")

def test_bitstringstatuslistentry_11():
    allure.dynamic.title("11 If present, the statusMessage property MUST be an array, the length of which MUST equal the number of possible status messages indicated by statusSize (e.g., statusMessage array MUST have 2 elements if statusSize has 1 bit, 4 elements if statusSize has 2 bits, 8 elements if statusSize has 3 bits, etc.)")
    allure.dynamic.link("https://www.w3.org/TR/vc-bitstring-status-list/#:~:text=If%20present%2C%20the%20statusMessage%20property%20MUST%20be%20an%20array%2C%20the%20length%20of%20which%20MUST%20equal%20the%20number%20of%20possible%20status%20messages%20indicated%20by%20statusSize%20%28e.g.%2C%20statusMessage%20array%20MUST%20have%202%20elements%20if%20statusSize%20has%201%20bit%2C%204%20elements%20if%20statusSize%20has%202%20bits%2C%208%20elements%20if%20statusSize%20has%203%20bits%2C%20etc.%29", name="Specification")
    allure.dynamic.parent_suite("Bitstring Status List v1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("00 Bitstringstatuslistentry")
    pytest.skip("TBD")

def test_bitstringstatuslistentry_12():
    allure.dynamic.title("12 statusMessage MAY be present if statusSize is 1, and MUST be present if statusSize is greater than 1")
    allure.dynamic.link("https://www.w3.org/TR/vc-bitstring-status-list/#:~:text=statusMessage%20MAY%20be%20present%20if%20statusSize%20is%201%2C%20and%20MUST%20be%20present%20if%20statusSize%20is%20greater%20than%201", name="Specification")
    allure.dynamic.parent_suite("Bitstring Status List v1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("00 Bitstringstatuslistentry")
    pytest.skip("TBD")

def test_bitstringstatuslistentry_13():
    allure.dynamic.title("13 If the statusMessage array is present, each element MUST contain the two properties described below, and MAY contain additional properties")
    allure.dynamic.link("https://www.w3.org/TR/vc-bitstring-status-list/#:~:text=If%20the%20statusMessage%20array%20is%20present%2C%20each%20element%20MUST%20contain%20the%20two%20properties%20described%20below%2C%20and%20MAY%20contain%20additional%20properties", name="Specification")
    allure.dynamic.parent_suite("Bitstring Status List v1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("00 Bitstringstatuslistentry")
    pytest.skip("TBD")

def test_bitstringstatuslistentry_14():
    allure.dynamic.title("14 If present, its value MUST be a URL or an array of URLs [URL] which dereference to material related to the status")
    allure.dynamic.link("https://www.w3.org/TR/vc-bitstring-status-list/#:~:text=If%20present%2C%20its%20value%20MUST%20be%20a%20URL%20or%20an%20array%20of%20URLs%20%5BURL%5D%20which%20dereference%20to%20material%20related%20to%20the%20status", name="Specification")
    allure.dynamic.parent_suite("Bitstring Status List v1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("00 Bitstringstatuslistentry")
    pytest.skip("TBD")

def test_bitstringstatuslistcredential_0():
    allure.dynamic.title("00 When a status list verifiable credential is published, it MUST be a conforming document, as defined in [VC-DATA-MODEL-2.0], that expresses the data model in this section")
    allure.dynamic.link("https://www.w3.org/TR/vc-bitstring-status-list/#:~:text=When%20a%20status%20list%20verifiable%20credential%20is%20published%2C%20it%20MUST%20be%20a%20conforming%20document%2C%20as%20defined%20in%20%5BVC%2DDATA%2DMODEL%2D2.0%5D%2C%20that%20expresses%20the%20data%20model%20in%20this%20section", name="Specification")
    allure.dynamic.parent_suite("Bitstring Status List v1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("01 Bitstringstatuslistcredential")
    pytest.skip("TBD")

def test_bitstringstatuslistcredential_1():
    allure.dynamic.title("01 One way to resolve this conflict is to remove ttl and specify that caching behavior can be expressed using protocol mechanisms (such as the expires header in HTTP), and that any caching performed MUST align with the validUntil value for the verifiable credential")
    allure.dynamic.link("https://www.w3.org/TR/vc-bitstring-status-list/#:~:text=One%20way%20to%20resolve%20this%20conflict%20is%20to%20remove%20ttl%20and%20specify%20that%20caching%20behavior%20can%20be%20expressed%20using%20protocol%20mechanisms%20%28such%20as%20the%20expires%20header%20in%20HTTP%29%2C%20and%20that%20any%20caching%20performed%20MUST%20align%20with%20the%20validUntil%20value%20for%20the%20verifiable%20credential", name="Specification")
    allure.dynamic.parent_suite("Bitstring Status List v1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("01 Bitstringstatuslistcredential")
    pytest.skip("TBD")

def test_bitstringstatuslistcredential_2():
    allure.dynamic.title("02 The verifiable credential that contains the status list MUST express a type property that includes the BitstringStatusListCredential value.")
    allure.dynamic.link("https://www.w3.org/TR/vc-bitstring-status-list/#:~:text=The%20verifiable%20credential%20that%20contains%20the%20status%20list%20MUST%20express%20a%20type%20property%20that%20includes%20the%20BitstringStatusListCredential%20value.", name="Specification")
    allure.dynamic.parent_suite("Bitstring Status List v1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("01 Bitstringstatuslistcredential")
    pytest.skip("TBD")

def test_bitstringstatuslistcredential_3():
    allure.dynamic.title("03 The type of the credential subject, which is the status list, MUST be BitstringStatusList.")
    allure.dynamic.link("https://www.w3.org/TR/vc-bitstring-status-list/#:~:text=The%20type%20of%20the%20credential%20subject%2C%20which%20is%20the%20status%20list%2C%20MUST%20be%20BitstringStatusList.", name="Specification")
    allure.dynamic.parent_suite("Bitstring Status List v1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("01 Bitstringstatuslistcredential")
    pytest.skip("TBD")

def test_bitstringstatuslistcredential_4():
    allure.dynamic.title("04 The value of the purpose property of the status entry, statusPurpose, MUST be one or more strings")
    allure.dynamic.link("https://www.w3.org/TR/vc-bitstring-status-list/#:~:text=The%20value%20of%20the%20purpose%20property%20of%20the%20status%20entry%2C%20statusPurpose%2C%20MUST%20be%20one%20or%20more%20strings", name="Specification")
    allure.dynamic.parent_suite("Bitstring Status List v1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("01 Bitstringstatuslistcredential")
    pytest.skip("TBD")

def test_bitstringstatuslistcredential_5():
    allure.dynamic.title("05 While the value of each string is arbitrary, the following values MUST be used for their intended purpose: Value Description revocation Used to cancel the validity of a verifiable credential")
    allure.dynamic.link("https://www.w3.org/TR/vc-bitstring-status-list/#:~:text=While%20the%20value%20of%20each%20string%20is%20arbitrary%2C%20the%20following%20values%20MUST%20be%20used%20for%20their%20intended%20purpose%3A%20Value%20Description%20revocation%20Used%20to%20cancel%20the%20validity%20of%20a%20verifiable%20credential", name="Specification")
    allure.dynamic.parent_suite("Bitstring Status List v1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("01 Bitstringstatuslistcredential")
    pytest.skip("TBD")

def test_bitstringstatuslistcredential_6():
    allure.dynamic.title("06 The status message descriptions MUST be defined in credentialSubject.statusMessages")
    allure.dynamic.link("https://www.w3.org/TR/vc-bitstring-status-list/#:~:text=The%20status%20message%20descriptions%20MUST%20be%20defined%20in%20credentialSubject.statusMessages", name="Specification")
    allure.dynamic.parent_suite("Bitstring Status List v1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("01 Bitstringstatuslistcredential")
    pytest.skip("TBD")

def test_bitstringstatuslistcredential_7():
    allure.dynamic.title("07 credentialSubject.statusSize MUST be specified when this statusPurpose value is used.")
    allure.dynamic.link("https://www.w3.org/TR/vc-bitstring-status-list/#:~:text=credentialSubject.statusSize%20MUST%20be%20specified%20when%20this%20statusPurpose%20value%20is%20used.", name="Specification")
    allure.dynamic.parent_suite("Bitstring Status List v1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("01 Bitstringstatuslistcredential")
    pytest.skip("TBD")

def test_bitstringstatuslistcredential_8():
    allure.dynamic.title("08 The encodedList property of the credential subject MUST be a Multibase-encoded base64url (with no padding) [RFC4648] representation of the GZIP-compressed [RFC1952] bitstring values for the associated range of verifiable credential status values")
    allure.dynamic.link("https://www.w3.org/TR/vc-bitstring-status-list/#:~:text=The%20encodedList%20property%20of%20the%20credential%20subject%20MUST%20be%20a%20Multibase%2Dencoded%20base64url%20%28with%20no%20padding%29%20%5BRFC4648%5D%20representation%20of%20the%20GZIP%2Dcompressed%20%5BRFC1952%5D%20bitstring%20values%20for%20the%20associated%20range%20of%20verifiable%20credential%20status%20values", name="Specification")
    allure.dynamic.parent_suite("Bitstring Status List v1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("01 Bitstringstatuslistcredential")
    pytest.skip("TBD")

def test_bitstringstatuslistcredential_9():
    allure.dynamic.title("09 The uncompressed bitstring MUST be at least 16KB in size")
    allure.dynamic.link("https://www.w3.org/TR/vc-bitstring-status-list/#:~:text=The%20uncompressed%20bitstring%20MUST%20be%20at%20least%2016KB%20in%20size", name="Specification")
    allure.dynamic.parent_suite("Bitstring Status List v1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("01 Bitstringstatuslistcredential")
    pytest.skip("TBD")

def test_bitstringstatuslistcredential_10():
    allure.dynamic.title("10 The bitstring MUST be encoded such that the first index, with a value of zero (0), is located at the left-most bit in the bitstring and the last index, with a value of one less than the length of the bitstring (bitstring_length - 1), is located at the right-most bit in the bitstring")
    allure.dynamic.link("https://www.w3.org/TR/vc-bitstring-status-list/#:~:text=The%20bitstring%20MUST%20be%20encoded%20such%20that%20the%20first%20index%2C%20with%20a%20value%20of%20zero%20%280%29%2C%20is%20located%20at%20the%20left%2Dmost%20bit%20in%20the%20bitstring%20and%20the%20last%20index%2C%20with%20a%20value%20of%20one%20less%20than%20the%20length%20of%20the%20bitstring%20%28bitstring_length%20%2D%201%29%2C%20is%20located%20at%20the%20right%2Dmost%20bit%20in%20the%20bitstring", name="Specification")
    allure.dynamic.parent_suite("Bitstring Status List v1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("01 Bitstringstatuslistcredential")
    pytest.skip("TBD")

def test_bitstringstatuslistcredential_11():
    allure.dynamic.title("11 If not present, implementers MUST use a value of 300000 for this property")
    allure.dynamic.link("https://www.w3.org/TR/vc-bitstring-status-list/#:~:text=If%20not%20present%2C%20implementers%20MUST%20use%20a%20value%20of%20300000%20for%20this%20property", name="Specification")
    allure.dynamic.parent_suite("Bitstring Status List v1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("01 Bitstringstatuslistcredential")
    pytest.skip("TBD")

def test_bitstringstatuslistcredential_12():
    allure.dynamic.title("12 A verifier MUST NOT use a cached BitstringStatusListCredential that was cached for more than the ttl duration prior to the start of verification operation on a verifiable credential")
    allure.dynamic.link("https://www.w3.org/TR/vc-bitstring-status-list/#:~:text=A%20verifier%20MUST%20NOT%20use%20a%20cached%20BitstringStatusListCredential%20that%20was%20cached%20for%20more%20than%20the%20ttl%20duration%20prior%20to%20the%20start%20of%20verification%20operation%20on%20a%20verifiable%20credential", name="Specification")
    allure.dynamic.parent_suite("Bitstring Status List v1.0")
    allure.dynamic.suite("01 Data model")
    allure.dynamic.sub_suite("01 Bitstringstatuslistcredential")
    pytest.skip("TBD")

def test_generate_algorithm_0():
    allure.dynamic.title("00 The following process, or one generating the exact output, MUST be followed when producing a BitstringStatusListCredential")
    allure.dynamic.link("https://www.w3.org/TR/vc-bitstring-status-list/#:~:text=The%20following%20process%2C%20or%20one%20generating%20the%20exact%20output%2C%20MUST%20be%20followed%20when%20producing%20a%20BitstringStatusListCredential", name="Specification")
    allure.dynamic.parent_suite("Bitstring Status List v1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("00 Generate algorithm")
    pytest.skip("TBD")

def test_validate_algorithm_0():
    allure.dynamic.title("00 The following process, or one generating the exact output, MUST be followed when validating a verifiable credential that is contained in a BitstringStatusListCredential")
    allure.dynamic.link("https://www.w3.org/TR/vc-bitstring-status-list/#:~:text=The%20following%20process%2C%20or%20one%20generating%20the%20exact%20output%2C%20MUST%20be%20followed%20when%20validating%20a%20verifiable%20credential%20that%20is%20contained%20in%20a%20BitstringStatusListCredential", name="Specification")
    allure.dynamic.parent_suite("Bitstring Status List v1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("01 Validate algorithm")
    pytest.skip("TBD")

def test_validate_algorithm_1():
    allure.dynamic.title("01 If the credentialIndex multiplied by the size is a value outside of the range of the bitstring, a RANGE_ERROR MUST be raised.")
    allure.dynamic.link("https://www.w3.org/TR/vc-bitstring-status-list/#:~:text=If%20the%20credentialIndex%20multiplied%20by%20the%20size%20is%20a%20value%20outside%20of%20the%20range%20of%20the%20bitstring%2C%20a%20RANGE_ERROR%20MUST%20be%20raised.", name="Specification")
    allure.dynamic.parent_suite("Bitstring Status List v1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("01 Validate algorithm")
    pytest.skip("TBD")

def test_validate_algorithm_2():
    allure.dynamic.title("02 If such a feature is supported, and if query parameters are supported by the URL scheme, then the name of the query parameter MUST be timestamp and the value MUST be a valid URL-encoded [XMLSCHEMA11-2] dateTimeStamp string value")
    allure.dynamic.link("https://www.w3.org/TR/vc-bitstring-status-list/#:~:text=If%20such%20a%20feature%20is%20supported%2C%20and%20if%20query%20parameters%20are%20supported%20by%20the%20URL%20scheme%2C%20then%20the%20name%20of%20the%20query%20parameter%20MUST%20be%20timestamp%20and%20the%20value%20MUST%20be%20a%20valid%20URL%2Dencoded%20%5BXMLSCHEMA11%2D2%5D%20dateTimeStamp%20string%20value", name="Specification")
    allure.dynamic.parent_suite("Bitstring Status List v1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("01 Validate algorithm")
    pytest.skip("TBD")

def test_validate_algorithm_3():
    allure.dynamic.title("03 The result of dereferencing such a timestamp-parameterized URL MUST be either a status list credential containing the status list as it existed at the given point in time, or a STATUS_RETRIEVAL_ERROR")
    allure.dynamic.link("https://www.w3.org/TR/vc-bitstring-status-list/#:~:text=The%20result%20of%20dereferencing%20such%20a%20timestamp%2Dparameterized%20URL%20MUST%20be%20either%20a%20status%20list%20credential%20containing%20the%20status%20list%20as%20it%20existed%20at%20the%20given%20point%20in%20time%2C%20or%20a%20STATUS_RETRIEVAL_ERROR", name="Specification")
    allure.dynamic.parent_suite("Bitstring Status List v1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("01 Validate algorithm")
    pytest.skip("TBD")

def test_bitstring_generation_algorithm_0():
    allure.dynamic.title("00 The following process, or one generating the exact output, MUST be followed when generating a status list bitstring")
    allure.dynamic.link("https://www.w3.org/TR/vc-bitstring-status-list/#:~:text=The%20following%20process%2C%20or%20one%20generating%20the%20exact%20output%2C%20MUST%20be%20followed%20when%20generating%20a%20status%20list%20bitstring", name="Specification")
    allure.dynamic.parent_suite("Bitstring Status List v1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("02 Bitstring generation algorithm")
    pytest.skip("TBD")

def test_bitstring_expansion_algorithm_0():
    allure.dynamic.title("00 The following process, or one generating the exact output, MUST be followed when expanding a compressed status list bitstring")
    allure.dynamic.link("https://www.w3.org/TR/vc-bitstring-status-list/#:~:text=The%20following%20process%2C%20or%20one%20generating%20the%20exact%20output%2C%20MUST%20be%20followed%20when%20expanding%20a%20compressed%20status%20list%20bitstring", name="Specification")
    allure.dynamic.parent_suite("Bitstring Status List v1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("03 Bitstring expansion algorithm")
    pytest.skip("TBD")

def test_processing_errors_0():
    allure.dynamic.title("00 The type value of the error object MUST be a URL that starts with the value https://www.w3.org/ns/credentials/status-list# and ends with the value in the section listed below.")
    allure.dynamic.link("https://www.w3.org/TR/vc-bitstring-status-list/#:~:text=The%20type%20value%20of%20the%20error%20object%20MUST%20be%20a%20URL%20that%20starts%20with%20the%20value%20https%3A//www.w3.org/ns/credentials/status%2Dlist%23%20and%20ends%20with%20the%20value%20in%20the%20section%20listed%20below.", name="Specification")
    allure.dynamic.parent_suite("Bitstring Status List v1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("04 Processing errors")
    pytest.skip("TBD")

def test_processing_errors_1():
    allure.dynamic.title("01 The code value MUST be the integer code described in the table below (in parentheses, beside the type name).")
    allure.dynamic.link("https://www.w3.org/TR/vc-bitstring-status-list/#:~:text=The%20code%20value%20MUST%20be%20the%20integer%20code%20described%20in%20the%20table%20below%20%28in%20parentheses%2C%20beside%20the%20type%20name%29.", name="Specification")
    allure.dynamic.parent_suite("Bitstring Status List v1.0")
    allure.dynamic.suite("02 Algorithms")
    allure.dynamic.sub_suite("04 Processing errors")
    pytest.skip("TBD")
