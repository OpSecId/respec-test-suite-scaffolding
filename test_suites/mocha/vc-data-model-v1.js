describe("Verifiable Credentials Data Model v1.1", 
    function() { 
    describe("00 Introduction", 
        function() { 
        describe("00 Conformance", 
            function() { 
            it("00 The key words MAY, MUST, MUST NOT, RECOMMENDED, and SHOULD in this document are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all capitals, as shown here.", 
                function() {
                this.skip('TBD');
            });
            it("01 Syntaxes of this document MUST be enforced", 
                function() {
                this.skip('TBD');
            });
            it("02 A serialization format for the conforming document MUST be deterministic, bi-directional, and lossless as described in Section 6", 
                function() {
                this.skip('TBD');
            });
            it("03 Conforming processors MUST produce errors when non-conforming documents are consumed.", 
                function() {
                this.skip('TBD');
            });
        });
    });
    describe("01 Basic concepts", 
        function() { 
        describe("00 Contexts", 
            function() { 
            it("00 Verifiable credentials and verifiable presentations MUST include a @context property.", 
                function() {
                this.skip('TBD');
            });
            it("01 The value of the @context property MUST be an ordered set where the first item is a URI with the value https://www.w3.org/2018/credentials/v1", 
                function() {
                this.skip('TBD');
            });
            it("02 Subsequent items in the array MUST express context information and be composed of any combination of URIs or objects", 
                function() {
                this.skip('TBD');
            });
            it("03 All libraries or processors MUST ensure that the order of the values in the @context property is what is expected for the specific application", 
                function() {
                this.skip('TBD');
            });
        });
        describe("01 Identifiers", 
            function() { 
            it("00 The id property MUST express an identifier that others are expected to use when expressing statements about a specific thing identified by that identifier.", 
                function() {
                this.skip('TBD');
            });
            it("01 The id property MUST NOT have more than one value.", 
                function() {
                this.skip('TBD');
            });
            it("02 The value of the id property MUST be a URI.", 
                function() {
                this.skip('TBD');
            });
            it("03 The value of the id property MUST be a single URI", 
                function() {
                this.skip('TBD');
            });
        });
        describe("02 Types", 
            function() { 
            it("00 Verifiable credentials and verifiable presentations MUST have a type property", 
                function() {
                this.skip('TBD');
            });
            it("01 The value of the type property MUST be, or map to (through interpretation of the @context property), one or more URIs", 
                function() {
                this.skip('TBD');
            });
            it("02 If more than one URI is provided, the URIs MUST be interpreted as an unordered set", 
                function() {
                this.skip('TBD');
            });
            it("03 With respect to this specification, the following table lists the objects that MUST have a type specified.", 
                function() {
                this.skip('TBD');
            });
            it("04 All credentials, presentations, and encapsulated objects MUST specify, or be associated with, additional more narrow types (like UniversityDegreeCredential, for example) so software systems can process this additional information.", 
                function() {
                this.skip('TBD');
            });
        });
        describe("03 Credential subject", 
            function() { 
            it("00 A verifiable credential MUST have a credentialSubject property.", 
                function() {
                this.skip('TBD');
            });
        });
        describe("04 Issuer", 
            function() { 
            it("00 A verifiable credential MUST have an issuer property.", 
                function() {
                this.skip('TBD');
            });
            it("01 The value of the issuer property MUST be either a URI or an object containing an id property", 
                function() {
                this.skip('TBD');
            });
        });
        describe("05 Issuance date", 
            function() { 
            it("00 A credential MUST have an issuanceDate property", 
                function() {
                this.skip('TBD');
            });
            it("01 The value of the issuanceDate property MUST be a string value of an [XMLSCHEMA11-2] combined date-time string representing the date and time the credential becomes valid, which could be a date and time in the future", 
                function() {
                this.skip('TBD');
            });
        });
        describe("06 Proofs signatures", 
            function() { 
            it("00 At least one proof mechanism, and the details necessary to evaluate that proof, MUST be expressed for a credential or presentation to be a verifiable credential or verifiable presentation; that is, to be verifiable.", 
                function() {
                this.skip('TBD');
            });
            it("01 When embedding a proof, the proof property MUST be used.", 
                function() {
                this.skip('TBD');
            });
            it("02 The specific method used for an embedded proof MUST be included using the type property.", 
                function() {
                this.skip('TBD');
            });
        });
        describe("07 Expiration", 
            function() { 
            it("00 If present, the value of the expirationDate property MUST be a string value of an [XMLSCHEMA11-2] date-time representing the date and time the credential ceases to be valid.", 
                function() {
                this.skip('TBD');
            });
        });
        describe("08 Status", 
            function() { 
            it("00 If present, the value of the credentialStatus property MUST include the following: id property, which MUST be a URI", 
                function() {
                this.skip('TBD');
            });
            it("01 id property, which MUST be a URI.", 
                function() {
                this.skip('TBD');
            });
        });
        describe("09 Presentations 0", 
            function() { 
            it("00 If present, the value of the verifiableCredential property MUST be constructed from one or more verifiable credentials, or of data derived from verifiable credentials in a cryptographically verifiable format.", 
                function() {
                this.skip('TBD');
            });
        });
    });
    describe("02 Advanced concepts", 
        function() { 
        describe("00 Extensibility", 
            function() { 
            it("00 JSON-based processors MUST process the @context key, ensuring the expected values exist in the expected order for the credential type being processed", 
                function() {
                this.skip('TBD');
            });
            it("01 JSON-LD-based processors MUST produce an error when a JSON-LD context redefines any term in the active context", 
                function() {
                this.skip('TBD');
            });
        });
        describe("01 Data schemas", 
            function() { 
            it("00 The value of the credentialSchema property MUST be one or more data schemas that provide verifiers with enough information to determine if the provided data conforms to the provided schema", 
                function() {
                this.skip('TBD');
            });
            it("01 Each credentialSchema MUST specify its type (for example, JsonSchemaValidator2018), and an id property that MUST be a URI identifying the schema file", 
                function() {
                this.skip('TBD');
            });
        });
        describe("02 Refreshing", 
            function() { 
            it("00 The value of the refreshService property MUST be one or more refresh services that provides enough information to the recipient's software such that the recipient can refresh the verifiable credential", 
                function() {
                this.skip('TBD');
            });
            it("01 Each refreshService value MUST specify its type (for example, ManualRefreshService2018) and its id, which is the URI of the service", 
                function() {
                this.skip('TBD');
            });
        });
        describe("03 Terms of use", 
            function() { 
            it("00 The value of the termsOfUse property MUST specify one or more terms of use policies under which the creator issued the credential or presentation", 
                function() {
                this.skip('TBD');
            });
            it("01 Each termsOfUse value MUST specify its type, for example, IssuerPolicy, and MAY specify its instance id", 
                function() {
                this.skip('TBD');
            });
        });
        describe("04 Evidence", 
            function() { 
            it("00 The value of the evidence property MUST be one or more evidence schemes providing enough information for a verifier to determine whether the evidence gathered by the issuer meets its confidence requirements for relying on the credential", 
                function() {
                this.skip('TBD');
            });
        });
        describe("05 Zero knowledge proofs", 
            function() { 
            it("00 The verifiable credential MUST contain a Proof, using the proof property, so that the holder can derive a verifiable presentation that reveals only the information than the holder intends to reveal.", 
                function() {
                this.skip('TBD');
            });
            it("01 If a credential definition is being used, the credential definition MUST be defined in the credentialSchema property, so that it can be used by all parties to perform various cryptographic operations in zero-knowledge.", 
                function() {
                this.skip('TBD');
            });
            it("02 Each derived verifiable credential within a verifiable presentation MUST contain all information necessary to verify the verifiable credential, either by including it directly within the credential, or by referencing the necessary information.", 
                function() {
                this.skip('TBD');
            });
            it("03 A verifiable presentation MUST NOT leak information that would enable the verifier to correlate the holder across multiple verifiable presentations.", 
                function() {
                this.skip('TBD');
            });
        });
    });
    describe("03 Syntaxes", 
        function() { 
        describe("00 Json", 
            function() { 
            it("00 Other values MUST be represented as a String type.", 
                function() {
                this.skip('TBD');
            });
        });
        describe("01 Proof formats", 
            function() { 
            it("00 vc: JSON object, which MUST be present in a JWT verifiable credential", 
                function() {
                this.skip('TBD');
            });
            it("01 vp: JSON object, which MUST be present in a JWT verifiable presentation", 
                function() {
                this.skip('TBD');
            });
            it("02 To encode a verifiable credential as a JWT, specific properties introduced by this specification MUST be either:", 
                function() {
                this.skip('TBD');
            });
            it("03 If no JWS is present, a proof property MUST be provided", 
                function() {
                this.skip('TBD');
            });
            it("04 For backward compatibility reasons, the issuer MUST use JWS to represent proofs based on a digital signature.", 
                function() {
                this.skip('TBD');
            });
            it("05 alg MUST be set for digital signatures", 
                function() {
                this.skip('TBD');
            });
            it("06 If only the proof property is needed for the chosen signature method (that is, if there is no choice of algorithm within that method), the alg header MUST be set to none.", 
                function() {
                this.skip('TBD');
            });
            it("07 typ, if present, MUST be set to JWT.", 
                function() {
                this.skip('TBD');
            });
            it("08 For backward compatibility with JWT processors, the following registered JWT claim names MUST be used, instead of or in addition to, their respective standard verifiable credential counterparts:", 
                function() {
                this.skip('TBD');
            });
            it("09 exp MUST represent the expirationDate property, encoded as a UNIX timestamp (NumericDate).", 
                function() {
                this.skip('TBD');
            });
            it("10 iss MUST represent the issuer property of a verifiable credential or the holder property of a verifiable presentation.", 
                function() {
                this.skip('TBD');
            });
            it("11 nbf MUST represent issuanceDate, encoded as a UNIX timestamp (NumericDate).", 
                function() {
                this.skip('TBD');
            });
            it("12 jti MUST represent the id property of the verifiable credential or verifiable presentation.", 
                function() {
                this.skip('TBD');
            });
            it("13 sub MUST represent the id property contained in the credentialSubject", 
                function() {
                this.skip('TBD');
            });
            it("14 aud MUST represent (i.e., identify) the intended audience of the verifiable presentation (i.e., the verifier intended by the presenting holder to receive and verify the verifiable presentation).", 
                function() {
                this.skip('TBD');
            });
            it("15 Additional verifiable credential claims MUST be added to the credentialSubject property of the JWT.", 
                function() {
                this.skip('TBD');
            });
            it("16 To decode a JWT to a standard credential or presentation, the following transformation MUST be performed:", 
                function() {
                this.skip('TBD');
            });
            it("17 To transform the JWT specific headers and claims, the following MUST be done:", 
                function() {
                this.skip('TBD');
            });
            it("18 If exp is present, the UNIX timestamp MUST be converted to an [XMLSCHEMA11-2] date-time, and MUST be used to set the value of the expirationDate property of credentialSubject of the new JSON object.", 
                function() {
                this.skip('TBD');
            });
            it("19 If iss is present, the value MUST be used to set the issuer property of the new credential JSON object or the holder property of the new presentation JSON object.", 
                function() {
                this.skip('TBD');
            });
            it("20 If nbf is present, the UNIX timestamp MUST be converted to an [XMLSCHEMA11-2] date-time, and MUST be used to set the value of the issuanceDate property of the new JSON object.", 
                function() {
                this.skip('TBD');
            });
            it("21 If sub is present, the value MUST be used to set the value of the id property of credentialSubject of the new credential JSON object.", 
                function() {
                this.skip('TBD');
            });
            it("22 If jti is present, the value MUST be used to set the value of the id property of the new JSON object.", 
                function() {
                this.skip('TBD');
            });
        });
    });
});