describe("Controller Documents 1.0", 
    function() { 
    describe("00 Introduction", 
        function() { 
        describe("00 Conformance", 
            function() { 
            it("00 The key words MAY, MUST, MUST NOT, OPTIONAL, RECOMMENDED, REQUIRED, and SHOULD in this document are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all capitals, as shown here.", 
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
        describe("00 Controller documents", 
            function() { 
            it("00 The value of id MUST be a string that conforms to the rules in the URL Standard.", 
                function() {
                this.skip('TBD');
            });
            it("01 A controller document MUST contain an id value in the root map.", 
                function() {
                this.skip('TBD');
            });
            it("02 If present, its value MUST be a string or a set of strings, each of which conforms to the rules in the URL Standard", 
                function() {
                this.skip('TBD');
            });
            it("03 If the controller property is not present, the value expressed by the id property MUST be treated as if it were also set as the value of the controller property.", 
                function() {
                this.skip('TBD');
            });
            it("04 If present, its value MUST be a set where each item in the set is a URI conforming to [RFC3986].", 
                function() {
                this.skip('TBD');
            });
        });
        describe("01 Verification methods", 
            function() { 
            it("00 If present, the value MUST be a set of verification methods, where each verification method is expressed using a map", 
                function() {
                this.skip('TBD');
            });
            it("01 The verification method map MUST include the id, type, controller, and specific verification material properties that are determined by the value of type and are defined in 2.2.1 Verification Material", 
                function() {
                this.skip('TBD');
            });
            it("02 The value of the id property for a verification method MUST be a string that conforms to the [URL] syntax.", 
                function() {
                this.skip('TBD');
            });
            it("03 The value of the type property MUST be a string that references exactly one verification method type.", 
                function() {
                this.skip('TBD');
            });
            it("04 The value of the controller property MUST be a string that conforms to the [URL] syntax.", 
                function() {
                this.skip('TBD');
            });
            it("05 If present, it MUST be an [XMLSCHEMA11-2] dateTimeStamp string specifying when the verification method SHOULD cease to be used", 
                function() {
                this.skip('TBD');
            });
            it("06 A verification method MUST NOT contain multiple verification material properties for the same material", 
                function() {
                this.skip('TBD');
            });
            it("07 As an internal implementation detail, such conversion MUST NOT affect the external representation of key material.", 
                function() {
                this.skip('TBD');
            });
            it("08 The value of the type property MUST contain the string Multikey.", 
                function() {
                this.skip('TBD');
            });
            it("09 If present, its value MUST be a Multibase encoded value as described in Section 2.4 Multibase.", 
                function() {
                this.skip('TBD');
            });
            it("10 The Multikey encoding of a P-256 public key MUST start with the two-byte prefix 0x8024 (the varint expression of 0x1200) followed by the 33-byte compressed public key data", 
                function() {
                this.skip('TBD');
            });
            it("11 The resulting 35-byte value MUST then be encoded using the base-58-btc alphabet, according to Section 2.4 Multibase, and then prepended with the base-58-btc Multibase header (z).", 
                function() {
                this.skip('TBD');
            });
            it("12 The encoding of a P-384 public key MUST start with the two-byte prefix 0x8124 (the varint expression of 0x1201) followed by the 49-byte compressed public key data", 
                function() {
                this.skip('TBD');
            });
            it("13 The encoding of an Ed25519 public key MUST start with the two-byte prefix 0xed01 (the varint expression of 0xed), followed by the 32-byte public key data", 
                function() {
                this.skip('TBD');
            });
            it("14 The resulting 34-byte value MUST then be encoded using the base-58-btc alphabet, according to Section 2.4 Multibase, and then prepended with the base-58-btc Multibase header (z).", 
                function() {
                this.skip('TBD');
            });
            it("15 The encoding of an BLS12-381 public key in the G2 group MUST start with the two-byte prefix 0xeb01 (the varint expression of 0xeb), followed by the 96-byte compressed public key data", 
                function() {
                this.skip('TBD');
            });
            it("16 The resulting 98-byte value MUST then be encoded using the base-58-btc alphabet, according to Section 2.4 Multibase, and then prepended with the base-58-btc Multibase header (z).", 
                function() {
                this.skip('TBD');
            });
            it("17 The Multikey encoding of a P-256 secret key MUST start with the two-byte prefix 0x8626 (the varint expression of 0x1306) followed by the 32-byte secret key data", 
                function() {
                this.skip('TBD');
            });
            it("18 The encoding of a P-384 secret key MUST start with the two-byte prefix 0x8726 (the varint expression of 0x1307) followed by the 48-byte secret key data", 
                function() {
                this.skip('TBD');
            });
            it("19 The encoding of an Ed25519 secret key MUST start with the two-byte prefix 0x8026 (the varint expression of 0x1300), followed by the 32-byte secret key data", 
                function() {
                this.skip('TBD');
            });
            it("20 The encoding of an BLS12-381 secret key in the G2 group MUST start with the two-byte prefix 0x8030 (the varint expression of 0x130a), followed by the 96-byte compressed public key data", 
                function() {
                this.skip('TBD');
            });
            it("21 When defining values for use with publicKeyMultibase and secretKeyMultibase, specification authors MAY define additional header values for other key types in other specifications and MUST NOT define alternate encodings for key types already defined by this specification.", 
                function() {
                this.skip('TBD');
            });
            it("22 The value of the type property MUST contain the string JsonWebKey.", 
                function() {
                this.skip('TBD');
            });
            it("23 If present, its value MUST be a map representing a JSON Web Key that conforms to [RFC7517]", 
                function() {
                this.skip('TBD');
            });
            it("24 The map MUST NOT include any members of the private information class, such as d, as described in the JWK Registration Template", 
                function() {
                this.skip('TBD');
            });
            it("25 As specified in Section 6.2.1.1 of the JWA specification, describing a key using an elliptic curve, the REQUIRED crv property is used to identify the particular curve type of the public key", 
                function() {
                this.skip('TBD');
            });
            it("26 It MUST NOT be used if the data structure containing it is public or may be revealed to parties other than the legitimate holders of the secret key.", 
                function() {
                this.skip('TBD');
            });
            it("27 The publicKeyJwk property MUST NOT contain any property marked as 'Private' or 'Secret' in any registry contained in the JOSE Registries [JOSE-REGISTRIES], including 'd'.", 
                function() {
                this.skip('TBD');
            });
        });
        describe("02 Verification relationships", 
            function() { 
            it("00 If present, its value MUST be a set of one or more verification methods", 
                function() {
                this.skip('TBD');
            });
            it("01 If present, its associated value MUST be a set of one or more verification methods", 
                function() {
                this.skip('TBD');
            });
            it("02 If present, the associated value MUST be a set of one or more verification methods", 
                function() {
                this.skip('TBD');
            });
        });
        describe("03 Multibase 0", 
            function() { 
            it("00 To base-encode a binary value into a Multibase string, an implementation MUST apply the algorithm in Section 3.1 Base Encode to the binary value, with the desired base encoding and alphabet from the table above, ensuring to prepend the associated Multibase header from the table above to the result", 
                function() {
                this.skip('TBD');
            });
            it("01 To base-decode a Multibase string, an implementation MUST apply the algorithm in Section 3.2 Base Decode to the string following the first character (Multibase header), with the alphabet associated with the Multibase header", 
                function() {
                this.skip('TBD');
            });
        });
        describe("04 Multihash", 
            function() { 
            it("00 To encode to a Multihash value, an implementation MUST concatenate the associated Multihash header, the cryptographic hash length, and the cryptographic hash value, in that order.", 
                function() {
                this.skip('TBD');
            });
            it("01 To decode a Multihash value, an implementation MUST 1) remove the prepended Multihash header value, which identifies the type of cryptographic hashing algorithm, 2) remove the output length, and 3) extract the raw cryptographic hash value which MUST match the expected output length associated with the Multihash header as well as the output length provided in the Multihash value itself.", 
                function() {
                this.skip('TBD');
            });
        });
    });
    describe("02 Algorithms", 
        function() { 
        describe("00 Base encode", 
            function() { 
            it("00 All mathematical operations MUST be performed using integer arithmetic", 
                function() {
                this.skip('TBD');
            });
        });
        describe("01 Base decode", 
            function() { 
            it("00 All mathematical operations MUST be performed using integer arithmetic", 
                function() {
                this.skip('TBD');
            });
        });
        describe("02 Retrieve verification method", 
            function() { 
            it("00 If vmIdentifier is not a valid URL, an error MUST be raised and SHOULD convey an error type of INVALID_VERIFICATION_METHOD_URL.", 
                function() {
                this.skip('TBD');
            });
            it("01 If controllerDocument.id does not match the controllerDocumentUrl, an error MUST be raised and SHOULD convey an error type of INVALID_CONTROLLER_DOCUMENT_ID.", 
                function() {
                this.skip('TBD');
            });
            it("02 If controllerDocument is not a conforming controller document, an error MUST be raised and SHOULD convey an error type of INVALID_CONTROLLER_DOCUMENT.", 
                function() {
                this.skip('TBD');
            });
            it("03 If verificationMethod is not a conforming verification method, an error MUST be raised and SHOULD convey an error type of INVALID_VERIFICATION_METHOD.", 
                function() {
                this.skip('TBD');
            });
            it("04 If the verification method is not associated with a verification relationship array in the controllerDocument, either by reference (URL) or by value (object), an error MUST be raised and SHOULD convey an error type of INVALID_RELATIONSHIP_FOR_VERIFICATION_METHOD.", 
                function() {
                this.skip('TBD');
            });
        });
        describe("03 Processing errors", 
            function() { 
            it("00 The type value of the error object MUST be a URL that starts with the value https://w3id.org/security# and ends with the value in the section listed below.", 
                function() {
                this.skip('TBD');
            });
            it("01 The code value MUST be the integer code described in the table below (in parentheses, beside the type name).", 
                function() {
                this.skip('TBD');
            });
        });
    });
    describe("03 Contexts and vocabularies", 
        function() { 
        describe("00 Context injection", 
            function() { 
            it("00 If an @context property is not provided in a document that is being secured or verified, or any Data Integrity terms used in the document are not mapped by existing values in the @context property, implementations using JSON-LD MUST inject or add an @context property with a value of https://www.w3.org/ns/controller/v1.", 
                function() {
                this.skip('TBD');
            });
        });
    });
});