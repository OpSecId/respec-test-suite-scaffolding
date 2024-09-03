describe("Data Integrity ECDSA Cryptosuites v1.0", 
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
            it("00 The Multikey encoding of a P-256 public key MUST start with the two-byte prefix 0x8024 (the varint expression of 0x1200) followed by the 33-byte compressed public key data", 
                function() {
                this.skip('TBD');
            });
            it("01 The resulting 35-byte value MUST then be encoded using the base-58-btc alphabet, according to the Multibase section in the [controller-document] specification, and then prepended with the base-58-btc Multibase header (z).", 
                function() {
                this.skip('TBD');
            });
            it("02 The encoding of a P-384 public key MUST start with the two-byte prefix 0x8124 (the varint expression of 0x1201) followed by the 49-byte compressed public key data", 
                function() {
                this.skip('TBD');
            });
            it("03 Any other encodings MUST NOT be allowed.", 
                function() {
                this.skip('TBD');
            });
            it("04 The encoding of a P-256 secret key MUST start with the two-byte prefix 0x8626 (the varint expression of 0x1306) followed by the 32-byte secret key data", 
                function() {
                this.skip('TBD');
            });
            it("05 The 34-byte value MUST then be encoded using the base-58-btc alphabet, according to the Multibase section in the [controller-document] specification, and then prepended with the base-58-btc Multibase header (z)", 
                function() {
                this.skip('TBD');
            });
            it("06 The 50-byte value MUST then be encoded using the base-58-btc alphabet, according to the Multibase section in the [controller-document] specification, and then prepended with the base-58-btc Multibase header (z)", 
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
            it("01 The cryptosuite property MUST be ecdsa-rdfc-2019, ecdsa-jcs-2019, or ecdsa-sd-2023.", 
                function() {
                this.skip('TBD');
            });
        });
    });
    describe("02 Algorithms", 
        function() { 
        describe("00 Ecdsa rdfc 2019", 
            function() { 
            it("00 The transformation options MUST contain a type identifier for the cryptographic suite (type) and a cryptosuite identifier (cryptosuite)", 
                function() {
                this.skip('TBD');
            });
            it("01 Whenever this algorithm encodes strings, it MUST use UTF-8 encoding.", 
                function() {
                this.skip('TBD');
            });
            it("02 If options.type is not set to the string DataIntegrityProof and options.cryptosuite is not set to the string ecdsa-rdfc-2019, an error MUST be raised and SHOULD convey an error type of PROOF_TRANSFORMATION_ERROR.", 
                function() {
                this.skip('TBD');
            });
            it("03 The proof options MUST contain a type identifier for the cryptographic suite (type) and MUST contain a cryptosuite identifier (cryptosuite)", 
                function() {
                this.skip('TBD');
            });
            it("04 If proofConfig.type is not set to DataIntegrityProof and/or proofConfig.cryptosuite is not set to ecdsa-rdfc-2019, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.", 
                function() {
                this.skip('TBD');
            });
            it("05 If proofConfig.created is set and if the value is not a valid [XMLSCHEMA11-2] datetime, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.", 
                function() {
                this.skip('TBD');
            });
            it("06 The proof options MUST contain a type identifier for the cryptographic suite (type) and MAY contain a cryptosuite identifier (cryptosuite)", 
                function() {
                this.skip('TBD');
            });
        });
        describe("01 Ecdsa jcs 2019", 
            function() { 
            it("00 The transformation options MUST contain a type identifier for the cryptographic suite (type) and a cryptosuite identifier (cryptosuite)", 
                function() {
                this.skip('TBD');
            });
            it("01 Whenever this algorithm encodes strings, it MUST use UTF-8 encoding.", 
                function() {
                this.skip('TBD');
            });
            it("02 If options.type is not set to the string DataIntegrityProof or options.cryptosuite is not set to the string ecdsa-jcs-2019, an error MUST be raised and SHOULD convey an error type of PROOF_TRANSFORMATION_ERROR.", 
                function() {
                this.skip('TBD');
            });
            it("03 The proof options MUST contain a type identifier for the cryptographic suite (type) and MUST contain a cryptosuite identifier (cryptosuite)", 
                function() {
                this.skip('TBD');
            });
            it("04 If proofConfig.type is not set to DataIntegrityProof and/or proofConfig.cryptosuite is not set to ecdsa-jcs-2019, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.", 
                function() {
                this.skip('TBD');
            });
            it("05 If proofConfig.created is set and if the value is not a valid [XMLSCHEMA11-2] datetime, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.", 
                function() {
                this.skip('TBD');
            });
            it("06 The proof options MUST contain a type identifier for the cryptographic suite (type) and MAY contain a cryptosuite identifier (cryptosuite)", 
                function() {
                this.skip('TBD');
            });
        });
        describe("02 Selective disclosure functions", 
            function() { 
            it("00 Note: All non-blank node identifiers in the path of any JSON Pointer MUST be included in the selection, this includes any root document identifier.", 
                function() {
                this.skip('TBD');
            });
            it("01 Note: The selection MUST include all types in the path of any JSON Pointer, including any root document type.", 
                function() {
                this.skip('TBD');
            });
            it("02 If value is now undefined, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR, indicating that the JSON pointer does not match the given document.", 
                function() {
                this.skip('TBD');
            });
        });
        describe("03 Ecdsa sd 2023 functions", 
            function() { 
            it("00 CBOR-encode components per [RFC8949] where CBOR tagging MUST NOT be used on any of the components", 
                function() {
                this.skip('TBD');
            });
            it("01 If the proofValue string does not start with u, indicating that it is a multibase-base64url-no-pad-encoded value, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.", 
                function() {
                this.skip('TBD');
            });
            it("02 If the decodedProofValue does not start with the ECDSA-SD base proof header bytes 0xd9, 0x5d, and 0x00, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.", 
                function() {
                this.skip('TBD');
            });
            it("03 If the decodedProofValue does not start with the ECDSA-SD disclosure proof header bytes 0xd9, 0x5d, and 0x01, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.", 
                function() {
                this.skip('TBD');
            });
            it("04 If the result is not an array of the following five elements — a byte array of length 64; a byte array of length 36; an array of byte arrays, each of length 64; a map of integers to byte arrays, each of length 32; and an array of integers — an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.", 
                function() {
                this.skip('TBD');
            });
        });
        describe("04 Ecdsa sd 2023", 
            function() { 
            it("00 The transformation options MUST contain a type identifier for the cryptographic suite (type), a cryptosuite identifier (cryptosuite), and a verification method (verificationMethod)", 
                function() {
                this.skip('TBD');
            });
            it("01 The transformation options MUST contain an array of mandatory JSON pointers (mandatoryPointers) and MAY contain additional options, such as a JSON-LD document loader", 
                function() {
                this.skip('TBD');
            });
            it("02 Whenever this algorithm encodes strings, it MUST use UTF-8 encoding.", 
                function() {
                this.skip('TBD');
            });
            it("03 Per the recommendations of [RFC2104], the HMAC key MUST be the same length as the digest size; for SHA-256, this is 256 bits or 32 bytes.", 
                function() {
                this.skip('TBD');
            });
            it("04 The proof options MUST contain a type identifier for the cryptographic suite (type) and MUST contain a cryptosuite identifier (cryptosuite)", 
                function() {
                this.skip('TBD');
            });
            it("05 If proofConfig.type is not set to DataIntegrityProof and/or proofConfig.cryptosuite is not set to ecdsa-sd-2023, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.", 
                function() {
                this.skip('TBD');
            });
            it("06 If proofConfig.created is set and if the value is not a valid [XMLSCHEMA11-2] datetime, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.", 
                function() {
                this.skip('TBD');
            });
            it("07 The proof options MUST contain a type identifier for the cryptographic suite (type) and MAY contain a cryptosuite identifier (cryptosuite)", 
                function() {
                this.skip('TBD');
            });
            it("08 If the length of signatures does not match the length of nonMandatory, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR, indicating that the signature count does not match the non-mandatory message count.", 
                function() {
                this.skip('TBD');
            });
        });
    });
});