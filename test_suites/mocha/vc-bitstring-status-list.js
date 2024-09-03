describe("Bitstring Status List v1.0", 
    function() { 
    describe("00 Introduction", 
        function() { 
        describe("00 Conformance", 
            function() { 
            it("00 The key words MAY, MUST, MUST NOT, SHOULD, and SHOULD NOT in this document are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all capitals, as shown here.", 
                function() {
                this.skip('TBD');
            });
            it("01 Conforming processors MUST produce errors when non-conforming documents are consumed.", 
                function() {
                this.skip('TBD');
            });
        });
    });
    describe("01 Data model", 
        function() { 
        describe("00 Bitstringstatuslistentry", 
            function() { 
            it("00 Any expression of the data model in this section MUST be expressed in a conforming verifiable credential as defined in [VC-DATA-MODEL-2.0].", 
                function() {
                this.skip('TBD');
            });
            it("01 It MUST NOT be the URL for the status list", 
                function() {
                this.skip('TBD');
            });
            it("02 The type property MUST be BitstringStatusListEntry.", 
                function() {
                this.skip('TBD');
            });
            it("03 The purpose of the status entry MUST be a string", 
                function() {
                this.skip('TBD');
            });
            it("04 While the value of the string is arbitrary, the following values MUST be used for their intended purpose: Value Description revocation Used to cancel the validity of a verifiable credential", 
                function() {
                this.skip('TBD');
            });
            it("05 The statusListIndex property MUST be an arbitrary size integer greater than or equal to 0, expressed as a string in base 10", 
                function() {
                this.skip('TBD');
            });
            it("06 The statusListCredential property MUST be a URL to a verifiable credential", 
                function() {
                this.skip('TBD');
            });
            it("07 When the URL is dereferenced, the resulting verifiable credential MUST have type property that includes the BitstringStatusListCredential value.", 
                function() {
                this.skip('TBD');
            });
            it("08 If statusSize is not present as a property of the credentialStatus, then statusSize MUST be processed as 1", 
                function() {
                this.skip('TBD');
            });
            it("09 If present, statusSize MUST be an integer greater than zero", 
                function() {
                this.skip('TBD');
            });
            it("10 If statusSize is provided and is greater than 1, then the property credentialStatus.statusMessage MUST be present, and the number of status messages MUST equal the number of possible values.", 
                function() {
                this.skip('TBD');
            });
            it("11 If present, the statusMessage property MUST be an array, the length of which MUST equal the number of possible status messages indicated by statusSize (e.g., statusMessage array MUST have 2 elements if statusSize has 1 bit, 4 elements if statusSize has 2 bits, 8 elements if statusSize has 3 bits, etc.)", 
                function() {
                this.skip('TBD');
            });
            it("12 statusMessage MAY be present if statusSize is 1, and MUST be present if statusSize is greater than 1", 
                function() {
                this.skip('TBD');
            });
            it("13 If the statusMessage array is present, each element MUST contain the two properties described below, and MAY contain additional properties", 
                function() {
                this.skip('TBD');
            });
            it("14 If present, its value MUST be a URL or an array of URLs [URL] which dereference to material related to the status", 
                function() {
                this.skip('TBD');
            });
        });
        describe("01 Bitstringstatuslistcredential", 
            function() { 
            it("00 When a status list verifiable credential is published, it MUST be a conforming document, as defined in [VC-DATA-MODEL-2.0], that expresses the data model in this section", 
                function() {
                this.skip('TBD');
            });
            it("01 One way to resolve this conflict is to remove ttl and specify that caching behavior can be expressed using protocol mechanisms (such as the expires header in HTTP), and that any caching performed MUST align with the validUntil value for the verifiable credential", 
                function() {
                this.skip('TBD');
            });
            it("02 The verifiable credential that contains the status list MUST express a type property that includes the BitstringStatusListCredential value.", 
                function() {
                this.skip('TBD');
            });
            it("03 The type of the credential subject, which is the status list, MUST be BitstringStatusList.", 
                function() {
                this.skip('TBD');
            });
            it("04 The value of the purpose property of the status entry, statusPurpose, MUST be one or more strings", 
                function() {
                this.skip('TBD');
            });
            it("05 While the value of each string is arbitrary, the following values MUST be used for their intended purpose: Value Description revocation Used to cancel the validity of a verifiable credential", 
                function() {
                this.skip('TBD');
            });
            it("06 The status message descriptions MUST be defined in credentialSubject.statusMessages", 
                function() {
                this.skip('TBD');
            });
            it("07 credentialSubject.statusSize MUST be specified when this statusPurpose value is used.", 
                function() {
                this.skip('TBD');
            });
            it("08 The encodedList property of the credential subject MUST be a Multibase-encoded base64url (with no padding) [RFC4648] representation of the GZIP-compressed [RFC1952] bitstring values for the associated range of verifiable credential status values", 
                function() {
                this.skip('TBD');
            });
            it("09 The uncompressed bitstring MUST be at least 16KB in size", 
                function() {
                this.skip('TBD');
            });
            it("10 The bitstring MUST be encoded such that the first index, with a value of zero (0), is located at the left-most bit in the bitstring and the last index, with a value of one less than the length of the bitstring (bitstring_length - 1), is located at the right-most bit in the bitstring", 
                function() {
                this.skip('TBD');
            });
            it("11 If not present, implementers MUST use a value of 300000 for this property", 
                function() {
                this.skip('TBD');
            });
            it("12 A verifier MUST NOT use a cached BitstringStatusListCredential that was cached for more than the ttl duration prior to the start of verification operation on a verifiable credential", 
                function() {
                this.skip('TBD');
            });
        });
    });
    describe("02 Algorithms", 
        function() { 
        describe("00 Generate algorithm", 
            function() { 
            it("00 The following process, or one generating the exact output, MUST be followed when producing a BitstringStatusListCredential", 
                function() {
                this.skip('TBD');
            });
        });
        describe("01 Validate algorithm", 
            function() { 
            it("00 The following process, or one generating the exact output, MUST be followed when validating a verifiable credential that is contained in a BitstringStatusListCredential", 
                function() {
                this.skip('TBD');
            });
            it("01 If the credentialIndex multiplied by the size is a value outside of the range of the bitstring, a RANGE_ERROR MUST be raised.", 
                function() {
                this.skip('TBD');
            });
            it("02 If such a feature is supported, and if query parameters are supported by the URL scheme, then the name of the query parameter MUST be timestamp and the value MUST be a valid URL-encoded [XMLSCHEMA11-2] dateTimeStamp string value", 
                function() {
                this.skip('TBD');
            });
            it("03 The result of dereferencing such a timestamp-parameterized URL MUST be either a status list credential containing the status list as it existed at the given point in time, or a STATUS_RETRIEVAL_ERROR", 
                function() {
                this.skip('TBD');
            });
        });
        describe("02 Bitstring generation algorithm", 
            function() { 
            it("00 The following process, or one generating the exact output, MUST be followed when generating a status list bitstring", 
                function() {
                this.skip('TBD');
            });
        });
        describe("03 Bitstring expansion algorithm", 
            function() { 
            it("00 The following process, or one generating the exact output, MUST be followed when expanding a compressed status list bitstring", 
                function() {
                this.skip('TBD');
            });
        });
        describe("04 Processing errors", 
            function() { 
            it("00 The type value of the error object MUST be a URL that starts with the value https://www.w3.org/ns/credentials/status-list# and ends with the value in the section listed below.", 
                function() {
                this.skip('TBD');
            });
            it("01 The code value MUST be the integer code described in the table below (in parentheses, beside the type name).", 
                function() {
                this.skip('TBD');
            });
        });
    });
});