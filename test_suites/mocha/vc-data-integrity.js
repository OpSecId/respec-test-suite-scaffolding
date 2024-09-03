describe("Verifiable Credential Data Integrity 1.0", 
    function() { 
    describe("00 Introduction", 
        function() { 
        describe("00 Conformance", 
            function() { 
            it("00 The key words MAY, MUST, OPTIONAL, and SHOULD in this document are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all capitals, as shown here.", 
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
        describe("00 Proofs", 
            function() { 
            it("00 When expressing a data integrity proof on an object, a proof property MUST be used", 
                function() {
                this.skip('TBD');
            });
            it("01 If present, its value MUST be either a single object, or an unordered set of objects, expressed using the properties below:", 
                function() {
                this.skip('TBD');
            });
            it("02 An optional identifier for the proof, which MUST be a URL [URL], such as a UUID as a URN (urn:uuid:6a1676b8-b51f-11ed-937b-d76685a20ff5)", 
                function() {
                this.skip('TBD');
            });
            it("03 The specific type of proof MUST be specified as a string that maps to a URL [URL]", 
                function() {
                this.skip('TBD');
            });
            it("04 The reason the proof was created MUST be specified as a string that maps to a URL [URL]", 
                function() {
                this.skip('TBD');
            });
            it("05 If included, the value MUST be a string that maps to a [URL]", 
                function() {
                this.skip('TBD');
            });
            it("06 If the proof type is DataIntegrityProof, cryptosuite MUST be specified; otherwise, cryptosuite MAY be specified", 
                function() {
                this.skip('TBD');
            });
            it("07 If specified, its value MUST be a string.", 
                function() {
                this.skip('TBD');
            });
            it("08 The date and time the proof was created is OPTIONAL and, if included, MUST be specified as an [XMLSCHEMA11-2] dateTimeStamp string, either in Universal Coordinated Time (UTC), denoted by a Z at the end of the value, or with a time zone offset relative to UTC", 
                function() {
                this.skip('TBD');
            });
            it("09 If present, it MUST be an [XMLSCHEMA11-2] dateTimeStamp string, either in Universal Coordinated Time (UTC), denoted by a Z at the end of the value, or with a time zone offset relative to UTC", 
                function() {
                this.skip('TBD');
            });
            it("10 If specified, the associated value MUST be either a string, or an unordered set of strings", 
                function() {
                this.skip('TBD');
            });
            it("11 The value MUST use a header and encoding as described in Section 2.4 Multibase of the Controller Documents 1.0 specification to express the binary data", 
                function() {
                this.skip('TBD');
            });
            it("12 Each value identifies another data integrity proof that MUST verify before the current proof is processed", 
                function() {
                this.skip('TBD');
            });
            it("13 If an unordered list, all referenced proofs in the array MUST verify", 
                function() {
                this.skip('TBD');
            });
        });
        describe("01 Resource integrity", 
            function() { 
            it("00 If present, the digestMultibase value MUST be a single string value, or an array of string values, each of which is a Multibase-encoded Multihash value.", 
                function() {
                this.skip('TBD');
            });
        });
        describe("02 Contexts and vocabularies", 
            function() { 
            it("00 Implementations that perform JSON-LD processing MUST treat the following JSON-LD context URLs as already resolved, where the resolved document matches the corresponding hash values below:", 
                function() {
                this.skip('TBD');
            });
            it("01 Implementations that perform RDF processing MUST treat the JSON-LD serialization of the vocabulary URL as already dereferenced, where the dereferenced document matches the corresponding hash value below.", 
                function() {
                this.skip('TBD');
            });
            it("02 Applications MUST use the algorithm in Section 4.6 Context Validation, or one that achieves equivalent protections, to validate contexts in a conforming secured document", 
                function() {
                this.skip('TBD');
            });
            it("03 Context validation MUST be run after running the applicable algorithm in either Section 4.4 Verify Proof or Section 4.5 Verify Proof Sets and Chains.", 
                function() {
                this.skip('TBD');
            });
            it("04 When securing a document, if an @context property is not provided in the document or the Data Integrity terms used in the document are not mapped by existing values in the @context property, implementations MUST inject or add an @context property with a value of https://w3id.org/security/data-integrity/v2.", 
                function() {
                this.skip('TBD');
            });
            it("05 Implementations that use JSON-LD processing, such as RDF Dataset Canonicalization [RDF-CANON], MUST throw an error, which SHOULD be DATA_LOSS_DETECTION_ERROR, when data is dropped by a JSON-LD processor, such as when an undefined term is detected in an input document.", 
                function() {
                this.skip('TBD');
            });
            it("06 When deserializing to RDF, implementations MUST ensure that the base URL is set to null.", 
                function() {
                this.skip('TBD');
            });
        });
    });
    describe("02 Cryptographic suites", 
        function() { 
        describe("00 Dataintegrityproof", 
            function() { 
            it("00 The type property MUST contain the string DataIntegrityProof.", 
                function() {
                this.skip('TBD');
            });
            it("01 The value of the cryptosuite property MUST be a string that identifies the cryptographic suite", 
                function() {
                this.skip('TBD');
            });
            it("02 If the processing environment supports subtypes of string, the type of the cryptosuite value MUST be the https://w3id.org/security#cryptosuiteString subtype of string.", 
                function() {
                this.skip('TBD');
            });
            it("03 The proofValue property MUST be used, as specified in 2.1 Proofs.", 
                function() {
                this.skip('TBD');
            });
            it("04 Cryptographic suite designers MUST use mandatory proof value properties defined in Section 2.1 Proofs, and MAY define other properties specific to their cryptographic suite.", 
                function() {
                this.skip('TBD');
            });
        });
    });
    describe("03 Algorithms", 
        function() { 
        describe("00 Add proof", 
            function() { 
            it("00 Whenever this algorithm encodes strings, it MUST use UTF-8 encoding.", 
                function() {
                this.skip('TBD');
            });
            it("01 If the algorithm produces an error, the error MUST be propagated and SHOULD convey the error type.", 
                function() {
                this.skip('TBD');
            });
            it("02 If one or more of the proof.type, proof.verificationMethod, and proof.proofPurpose values is not set, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.", 
                function() {
                this.skip('TBD');
            });
            it("03 If options has a non-null domain item, it MUST be equal to proof.domain or an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.", 
                function() {
                this.skip('TBD');
            });
            it("04 If options has a non-null challenge item, it MUST be equal to proof.challenge or an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.", 
                function() {
                this.skip('TBD');
            });
        });
        describe("01 Add proof set chain", 
            function() { 
            it("00 Whenever this algorithm encodes strings, it MUST use UTF-8 encoding.", 
                function() {
                this.skip('TBD');
            });
            it("01 If a proof with id equal to previousProof does not exist in allProofs, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.", 
                function() {
                this.skip('TBD');
            });
            it("02 If any element of previousProof array has an id attribute that does not match the id attribute of any element of allProofs, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.", 
                function() {
                this.skip('TBD');
            });
        });
        describe("02 Verify proof", 
            function() { 
            it("00 When a step says 'an error MUST be raised', it means that a verification result MUST be returned with a verified of false and a non-empty errors list.", 
                function() {
                this.skip('TBD');
            });
            it("01 If either securedDocument is not a map or securedDocument.proof is not a map, an error MUST be raised and SHOULD convey an error type of PARSING_ERROR.", 
                function() {
                this.skip('TBD');
            });
            it("02 If one or more of proof.type, proof.verificationMethod, and proof.proofPurpose does not exist, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.", 
                function() {
                this.skip('TBD');
            });
            it("03 If expectedProofPurpose was given, and it does not match proof.proofPurpose, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.", 
                function() {
                this.skip('TBD');
            });
            it("04 If domain was given, and it does not contain the same strings as proof.domain (treating a single string as a set containing just that string), an error MUST be raised and SHOULD convey an error type of INVALID_DOMAIN_ERROR.", 
                function() {
                this.skip('TBD');
            });
            it("05 If challenge was given, and it does not match proof.challenge, an error MUST be raised and SHOULD convey an error type of INVALID_CHALLENGE_ERROR.", 
                function() {
                this.skip('TBD');
            });
        });
        describe("03 Verify proof sets and chains", 
            function() { 
            it("00 If a proof with id does not exist in allProofs, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR", 
                function() {
                this.skip('TBD');
            });
            it("01 If any element of previousProof array has an id attribute that does not match the id attribute of any element of allProofs, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.", 
                function() {
                this.skip('TBD');
            });
        });
        describe("04 Processing errors", 
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
});