describe("Data Integrity EdDSA Cryptosuites v1.0", 
    function() { 
    describe("00 Introduction", 
        function() { 
        describe("00 Conformance", 
            function() { 
            it("00 The key words MAY, MUST, MUST NOT, and SHOULD in this document are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all capitals, as shown here.", 
                function() {
                this.skip('TBD');
            });
            it("01 Algorithms of this document MUST be enforced.", 
                function() {
                this.skip('TBD');
            });
            it("02 Conforming processors MUST produce errors when non-conforming documents are consumed.", 
                function() {
                this.skip('TBD');
            });
        });
    });
    describe("01 Data model", 
        function() { 
        describe("00 Verification methods", 
            function() { 
            it("00 The publicKeyMultibase value of the verification method MUST start with the base-58-btc prefix (z), as defined in the Multibase section of Controller Documents 1.0", 
                function() {
                this.skip('TBD');
            });
            it("01 A Multibase-encoded Multikey value follows, which MUST consist of a binary value that starts with the two-byte prefix 0xed01, which is the Multikey header for an Ed25519 public key, followed by the 32-byte public key data, all of which is then encoded using base-58-btc", 
                function() {
                this.skip('TBD');
            });
            it("02 Any other encoding MUST NOT be allowed.", 
                function() {
                this.skip('TBD');
            });
        });
        describe("01 Proof representations", 
            function() { 
            it("00 The type property MUST be DataIntegrityProof.", 
                function() {
                this.skip('TBD');
            });
            it("01 The cryptosuite property of the proof MUST be eddsa-rdfc-2022 or eddsa-jcs-2022.", 
                function() {
                this.skip('TBD');
            });
            it("02 The proofValue property of the proof MUST be a detached EdDSA signature produced according to [RFC8032], encoded using the base-58-btc header and alphabet as described in the Multibase section of Controller Documents 1.0.", 
                function() {
                this.skip('TBD');
            });
        });
    });
    describe("02 Algorithms", 
        function() { 
        describe("00 Eddsa rdfc 2022", 
            function() { 
            it("00 The transformation options MUST contain a type identifier for the cryptographic suite (type) and a cryptosuite identifier (cryptosuite)", 
                function() {
                this.skip('TBD');
            });
            it("01 Whenever this algorithm encodes strings, it MUST use UTF-8 encoding.", 
                function() {
                this.skip('TBD');
            });
            it("02 If options.type is not set to the string DataIntegrityProof and options.cryptosuite is not set to the string eddsa-rdfc-2022, an error MUST be raised that SHOULD convey an error type of PROOF_TRANSFORMATION_ERROR.", 
                function() {
                this.skip('TBD');
            });
            it("03 The proof options MUST contain a type identifier for the cryptographic suite (type) and MUST contain a cryptosuite identifier (cryptosuite)", 
                function() {
                this.skip('TBD');
            });
            it("04 If proofConfig.type is not set to DataIntegrityProof and/or proofConfig.cryptosuite is not set to eddsa-rdfc-2022, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.", 
                function() {
                this.skip('TBD');
            });
            it("05 If proofConfig.created is present and set to a value that is not a valid [XMLSCHEMA11-2] datetime, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.", 
                function() {
                this.skip('TBD');
            });
            it("06 The proof options MUST contain a type identifier for the cryptographic suite (type) and MAY contain a cryptosuite identifier (cryptosuite)", 
                function() {
                this.skip('TBD');
            });
        });
        describe("01 Eddsa jcs 2022", 
            function() { 
            it("00 The transformation options MUST contain a type identifier for the cryptographic suite (type) and a cryptosuite identifier (cryptosuite)", 
                function() {
                this.skip('TBD');
            });
            it("01 Whenever this algorithm encodes strings, it MUST use UTF-8 encoding.", 
                function() {
                this.skip('TBD');
            });
            it("02 If options.type is not set to the string DataIntegrityProof and options.cryptosuite is not set to the string eddsa-jcs-2022, an error MUST be raised that SHOULD convey an error type of PROOF_VERIFICATION_ERROR.", 
                function() {
                this.skip('TBD');
            });
            it("03 The proof options MUST contain a type identifier for the cryptographic suite (type) and MUST contain a cryptosuite identifier (cryptosuite)", 
                function() {
                this.skip('TBD');
            });
            it("04 If proofConfig.type is not set to DataIntegrityProof or proofConfig.cryptosuite is not set to eddsa-jcs-2022, an error MUST be raised that SHOULD convey an error type of PROOF_GENERATION_ERROR.", 
                function() {
                this.skip('TBD');
            });
            it("05 If proofConfig.created is set to a value that is not a valid [XMLSCHEMA11-2] datetime, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.", 
                function() {
                this.skip('TBD');
            });
            it("06 The proof options MUST contain a type identifier for the cryptographic suite (type) and MAY contain a cryptosuite identifier (cryptosuite)", 
                function() {
                this.skip('TBD');
            });
        });
    });
    describe("03 The ed25519signature2020 suite", 
        function() { 
        describe("00 Data model 0", 
            function() { 
            it("00 The type of the verification method MUST be Ed25519VerificationKey2020.", 
                function() {
                this.skip('TBD');
            });
            it("01 The controller of the verification method MUST be a URL.", 
                function() {
                this.skip('TBD');
            });
            it("02 The publicKeyMultibase value of the verification method MUST start with the base-58-btc prefix (z), as defined in the Multibase section of [VC-DATA-INTEGRITY]", 
                function() {
                this.skip('TBD');
            });
            it("03 A Multibase-encoded Multikey value follows, which MUST consist of a binary value that starts with the two-byte prefix 0xed01, which is the Multikey header for an Ed25519 public key, followed by the 32-byte public key data, all of which is then encoded using base-58-btc", 
                function() {
                this.skip('TBD');
            });
            it("04 Any other encoding MUST NOT be allowed.", 
                function() {
                this.skip('TBD');
            });
            it("05 The verificationMethod property of the proof MUST be a URL", 
                function() {
                this.skip('TBD');
            });
            it("06 Dereferencing the verificationMethod MUST result in an object containing a type property with the value set to Ed25519VerificationKey2020.", 
                function() {
                this.skip('TBD');
            });
            it("07 The type property of the proof MUST be Ed25519Signature2020.", 
                function() {
                this.skip('TBD');
            });
            it("08 The created property of the proof MUST be an [XMLSCHEMA11-2] formatted date string.", 
                function() {
                this.skip('TBD');
            });
            it("09 The proofPurpose property of the proof MUST be a string, and MUST match the verification relationship expressed by the verification method controller.", 
                function() {
                this.skip('TBD');
            });
            it("10 The proofValue property of the proof MUST be a detached EdDSA produced according to [RFC8032], encoded using the base-58-btc header and alphabet as described in the Multibase section of [VC-DATA-INTEGRITY].", 
                function() {
                this.skip('TBD');
            });
        });
        describe("01 Algorithms 0", 
            function() { 
            it("00 To generate a proof, the algorithm in Section 4.1: Add Proof in the Data Integrity [VC-DATA-INTEGRITY] specification MUST be executed", 
                function() {
                this.skip('TBD');
            });
            it("01 To verify a proof, the algorithm in Section 4.2: Verify Proof in the Data Integrity [VC-DATA-INTEGRITY] specification MUST be executed", 
                function() {
                this.skip('TBD');
            });
            it("02 The transformation options MUST contain a type identifier for the cryptographic suite (type) and a cryptosuite identifier (cryptosuite)", 
                function() {
                this.skip('TBD');
            });
            it("03 Whenever this algorithm encodes strings, it MUST use UTF-8 encoding.", 
                function() {
                this.skip('TBD');
            });
            it("04 If options.type is not set to the string Ed25519Signature2020, an error MUST be raised that SHOULD convey an error type of PROOF_TRANSFORMATION_ERROR.", 
                function() {
                this.skip('TBD');
            });
            it("05 The proof configuration MUST contain a type identifier for the cryptographic suite (type) and MAY contain a cryptosuite identifier (cryptosuite)", 
                function() {
                this.skip('TBD');
            });
            it("06 The proof options MUST contain a type identifier for the cryptographic suite (type) and MAY contain a cryptosuite identifier (cryptosuite)", 
                function() {
                this.skip('TBD');
            });
            it("07 If proofConfig.type is not set to Ed25519Signature2020, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.", 
                function() {
                this.skip('TBD');
            });
            it("08 If proofConfig.created is present and set to a value that is not a valid [XMLSCHEMA11-2] datetime, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.", 
                function() {
                this.skip('TBD');
            });
        });
    });
});