describe("Verifiable Credentials Data Model v2.0", 
    function() { 
    describe("00 Introduction", 
        function() { 
        describe("00 Conformance", 
            function() { 
            it("00 The key words MAY, MUST, MUST NOT, OPTIONAL, RECOMMENDED, REQUIRED, SHOULD, and SHOULD NOT in this document are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all capitals, as shown here.", 
                function() {
                this.skip('TBD');
            });
            it("01 A conforming document is a compacted JSON-LD document that complies with all of the relevant 'MUST' statements in this specification", 
                function() {
                this.skip('TBD');
            });
            it("02 Specifically, the relevant normative 'MUST' statements in Sections 4", 
                function() {
                this.skip('TBD');
            });
            it("03 Syntaxes of this document MUST be enforced", 
                function() {
                this.skip('TBD');
            });
            it("04 A conforming document MUST be either a verifiable credential with a media type of application/vc or a verifiable presentation with a media type of application/vp", 
                function() {
                this.skip('TBD');
            });
            it("05 A conforming document MUST be secured by at least one securing mechanism as described in Section 4.12 Securing Mechanisms.", 
                function() {
                this.skip('TBD');
            });
            it("06 A conforming issuer implementation produces conforming documents, MUST include all required properties in the conforming documents it produces, and MUST secure the conforming documents it produces using a securing mechanism described in Section 4.12 Securing Mechanisms.", 
                function() {
                this.skip('TBD');
            });
            it("07 A conforming verifier implementation consumes conforming documents, MUST perform verification on a conforming document as described in Section 4.12 Securing Mechanisms, MUST check that each required property satisfies the normative requirements for that property, and MUST produce errors when non-conforming documents are detected.", 
                function() {
                this.skip('TBD');
            });
        });
    });
    describe("01 Basic concepts", 
        function() { 
        describe("00 Contexts", 
            function() { 
            it("00 Verifiable credentials and verifiable presentations MUST include a @context property", 
                function() {
                this.skip('TBD');
            });
            it("01 Application developers MUST understand every JSON-LD context used by their application, at least to the extent that it affects the meaning of the terms used by their application", 
                function() {
                this.skip('TBD');
            });
            it("02 The value of the @context property MUST be an ordered set where the first item is a URL with the value https://www.w3.org/ns/credentials/v2", 
                function() {
                this.skip('TBD');
            });
            it("03 Subsequent items in the ordered set MUST be composed of any combination of URLs and objects, where each is processable as a JSON-LD Context.", 
                function() {
                this.skip('TBD');
            });
        });
        describe("01 Identifiers", 
            function() { 
            it("00 If present, id property's value MUST be a single URL, which MAY be dereferenceable", 
                function() {
                this.skip('TBD');
            });
        });
        describe("02 Types", 
            function() { 
            it("00 Verifiable credentials and verifiable presentations MUST contain a type property with an associated value.", 
                function() {
                this.skip('TBD');
            });
            it("01 The value of the type property MUST be one or more terms and absolute URL strings", 
                function() {
                this.skip('TBD');
            });
            it("02 Concerning this specification, the following table lists the objects that MUST have a type specified.", 
                function() {
                this.skip('TBD');
            });
        });
        describe("03 Names and descriptions", 
            function() { 
            it("00 If present, the value of the name property MUST be a string or a language value object as described in 11.1 Language and Base Direction", 
                function() {
                this.skip('TBD');
            });
            it("01 If present, the value of the description property MUST be a string or a language value object as described in 11.1 Language and Base Direction", 
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
            it("01 The value of the issuer property MUST be either a URL or an object containing an id property whose value is a URL; in either case, the issuer selects this URL to identify itself in a globally unambiguous way", 
                function() {
                this.skip('TBD');
            });
        });
        describe("05 Credential subject", 
            function() { 
            it("00 A verifiable credential MUST contain a credentialSubject property.", 
                function() {
                this.skip('TBD');
            });
            it("01 The value of the credentialSubject property is a set of objects where each object MUST be the subject of one or more claims, which MUST be serialized inside the credentialSubject property", 
                function() {
                this.skip('TBD');
            });
        });
        describe("06 Validity period", 
            function() { 
            it("00 If present, the value of the validFrom property MUST be a [XMLSCHEMA11-2] dateTimeStamp string value representing the date and time the credential becomes valid, which could be a date and time in the future or the past", 
                function() {
                this.skip('TBD');
            });
            it("01 If a validUntil value also exists, the validFrom value MUST express a point in time that is temporally the same or earlier than the point in time expressed by the validUntil value.", 
                function() {
                this.skip('TBD');
            });
            it("02 If present, the value of the validUntil property MUST be a [XMLSCHEMA11-2] dateTimeStamp string value representing the date and time the credential ceases to be valid, which could be a date and time in the past or the future", 
                function() {
                this.skip('TBD');
            });
            it("03 If a validFrom value also exists, the validUntil value MUST express a point in time that is temporally the same or later than the point in time expressed by the validFrom value.", 
                function() {
                this.skip('TBD');
            });
        });
        describe("07 Status", 
            function() { 
            it("00 If present, the normative guidance in Section 4.4 Identifiers MUST be followed.", 
                function() {
                this.skip('TBD');
            });
            it("01 The type property is REQUIRED", 
                function() {
                this.skip('TBD');
            });
            it("02 The related normative guidance in Section 4.5 Types MUST be followed.", 
                function() {
                this.skip('TBD');
            });
            it("03 Credential status specifications MUST NOT enable tracking of individuals, such as an issuer being notified (either directly or indirectly) when a verifier is interested in a specific holder or subject", 
                function() {
                this.skip('TBD');
            });
        });
        describe("08 Data schemas", 
            function() { 
            it("00 The value of the credentialSchema property MUST be one or more data schemas that provide verifiers with enough information to determine whether the provided data conforms to the provided schema(s)", 
                function() {
                this.skip('TBD');
            });
            it("01 Each credentialSchema MUST specify its type (for example, JsonSchema) and an id property that MUST be a URL identifying the schema file", 
                function() {
                this.skip('TBD');
            });
        });
        describe("09 Verifiable presentations", 
            function() { 
            it("00 If present, the normative guidance in Section 4.4 Identifiers MUST be followed.", 
                function() {
                this.skip('TBD');
            });
            it("01 The type property MUST be present", 
                function() {
                this.skip('TBD');
            });
            it("02 One value of this property MUST be VerifiablePresentation, but additional types MAY be included", 
                function() {
                this.skip('TBD');
            });
            it("03 The related normative guidance in Section 4.5 Types MUST be followed.", 
                function() {
                this.skip('TBD');
            });
            it("04 The value MUST be one or more verifiable credential and/or enveloped verifiable credential objects (the values MUST NOT be non-object values such as numbers, strings, or URLs)", 
                function() {
                this.skip('TBD');
            });
            it("05 These objects are called verifiable credential graphs and MUST express information that is secured using a securing mechanism", 
                function() {
                this.skip('TBD');
            });
            it("06 If present, the value MUST be either a URL or an object containing an id property", 
                function() {
                this.skip('TBD');
            });
            it("07 The @context property of the object MUST be present and include a context, such as the base context for this specification, that defines at least the id, type, and EnvelopedVerifiableCredential terms as defined by the base context provided by this specification", 
                function() {
                this.skip('TBD');
            });
            it("08 The id value of the object MUST be a data: URL [RFC2397] that expresses a secured verifiable credential using an enveloping security scheme, such as Securing Verifiable Credentials using JOSE and COSE [VC-JOSE-COSE]", 
                function() {
                this.skip('TBD');
            });
            it("09 The type value of the object MUST be EnvelopedVerifiableCredential.", 
                function() {
                this.skip('TBD');
            });
            it("10 The @context property of the object MUST be present and include a context, such as the base context for this specification, that defines at least the id, type, and EnvelopedVerifiablePresentation terms as defined by the base context provided by this specification", 
                function() {
                this.skip('TBD');
            });
            it("11 The id value of the object MUST be a data: URL [RFC2397] that expresses a secured verifiable presentation using an enveloping securing mechanism, such as Securing Verifiable Credentials using JOSE and COSE [VC-JOSE-COSE]", 
                function() {
                this.skip('TBD');
            });
            it("12 The type value of the object MUST be EnvelopedVerifiablePresentation.", 
                function() {
                this.skip('TBD');
            });
            it("13 A verifiable presentation that includes a self-asserted verifiable credential, which is secured only using the same mechanism as the verifiable presentation, MUST include a holder property.", 
                function() {
                this.skip('TBD');
            });
            it("14 When a self-asserted verifiable credential is secured using the same mechanism as the verifiable presentation, the value of the issuer property of the verifiable credential MUST be identical to the holder property of the verifiable presentation.", 
                function() {
                this.skip('TBD');
            });
        });
    });
    describe("02 Advanced concepts", 
        function() { 
        describe("00 Extensibility", 
            function() { 
            it("00 New terms MUST define a new URL for each term", 
                function() {
                this.skip('TBD');
            });
            it("01 When doing so, the general guidelines for [LINKED-DATA] are expected to be followed, in particular: Human-readable documentation MUST be published, describing the semantics of and the constraints on the use of each term", 
                function() {
                this.skip('TBD');
            });
            it("02 Human-readable documentation MUST be published, describing the semantics of and the constraints on the use of each term.", 
                function() {
                this.skip('TBD');
            });
            it("03 Furthermore, a machine-readable description (that is, a JSON-LD Context document) MUST be published at the URL specified in the @context property for the vocabulary", 
                function() {
                this.skip('TBD');
            });
            it("04 This context MUST map each term to its corresponding URL, possibly accompanied by further constraints like the type of the property value", 
                function() {
                this.skip('TBD');
            });
            it("05 If a conforming document does not use JSON-LD Contexts that define all terms used, it MUST include the https://www.w3.org/ns/credentials/undefined-terms/v2 as the last value in the @context property.", 
                function() {
                this.skip('TBD');
            });
        });
        describe("01 Integrity of related resources", 
            function() { 
            it("00 The value of the relatedResource property MUST be one or more objects of the following form: Property Description id The identifier for the resource is REQUIRED and conforms to the format defined in Section 4.4 Identifiers", 
                function() {
                this.skip('TBD');
            });
            it("01 The value MUST be unique among the list of related resource objects", 
                function() {
                this.skip('TBD');
            });
            it("02 Each object associated with relatedResource MUST contain at least a digestSRI or a digestMultibase value.", 
                function() {
                this.skip('TBD');
            });
            it("03 The identifier for the resource is REQUIRED and conforms to the format defined in Section 4.4 Identifiers", 
                function() {
                this.skip('TBD');
            });
            it("04 The value MUST be unique among the list of related resource objects.", 
                function() {
                this.skip('TBD');
            });
            it("05 If it is, the specification MUST produce a validation error unless the resource matches the expected media type and cryptographic digest.", 
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
            it("01 Each refreshService value MUST specify its type", 
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
            it("01 Each termsOfUse value MUST specify its type, for example, TrustFrameworkPolicy, and MAY specify its instance id", 
                function() {
                this.skip('TBD');
            });
        });
        describe("04 Evidence", 
            function() { 
            it("00 If present, the value of the evidence property MUST be either a single object or a set of one or more objects", 
                function() {
                this.skip('TBD');
            });
            it("01 If present, the normative guidance in Section 4.4 Identifiers MUST be followed", 
                function() {
                this.skip('TBD');
            });
            it("02 type The type property is REQUIRED", 
                function() {
                this.skip('TBD');
            });
            it("03 The related normative guidance in Section 4.5 Types MUST be followed.", 
                function() {
                this.skip('TBD');
            });
            it("04 If present, the normative guidance in Section 4.4 Identifiers MUST be followed.", 
                function() {
                this.skip('TBD');
            });
            it("05 The type property is REQUIRED", 
                function() {
                this.skip('TBD');
            });
        });
        describe("05 Zero knowledge proofs", 
            function() { 
            it("00 Specification authors that create securing mechanisms MUST NOT design them in such a way that they leak information that would enable the verifier to correlate a holder across multiple verifiable presentations to different verifiers.", 
                function() {
                this.skip('TBD');
            });
        });
        describe("06 Representing time", 
            function() { 
            it("00 Time values that are incorrectly serialized without an offset MUST be interpreted as UTC", 
                function() {
                this.skip('TBD');
            });
        });
        describe("07 Reserved extension points", 
            function() { 
            it("00 In order to avoid collisions regarding how the following properties are used, implementations MUST specify a type property in the value associated with the reserved property", 
                function() {
                this.skip('TBD');
            });
            it("01 The associated vocabulary URL MUST be https://www.w3.org/2018/credentials#confidenceMethod.", 
                function() {
                this.skip('TBD');
            });
            it("02 The associated vocabulary URL MUST be https://www.w3.org/2018/credentials#renderMethod.", 
                function() {
                this.skip('TBD');
            });
        });
        describe("08 Ecosystem compatibility", 
            function() { 
            it("00 MUST identify whether the transformation to this data model is one-way-only or round-trippable.", 
                function() {
                this.skip('TBD');
            });
            it("01 MUST preserve the @context values when performing round-trippable transformation.", 
                function() {
                this.skip('TBD');
            });
            it("02 MUST result in a conforming document when transforming to the data model described by this specification.", 
                function() {
                this.skip('TBD');
            });
            it("03 MUST specify a registered media type for the input document.", 
                function() {
                this.skip('TBD');
            });
        });
        describe("09 Securing mechanism specifications", 
            function() { 
            it("00 Securing mechanism specifications MUST document normative algorithms that provide content integrity protection for conforming documents", 
                function() {
                this.skip('TBD');
            });
            it("01 Securing mechanism specifications MUST provide a verification algorithm that returns the information in the conforming document that has been secured, in isolation, without including any securing mechanism information, such as proof or JOSE/COSE header parameters and signatures", 
                function() {
                this.skip('TBD');
            });
            it("02 A verification algorithm MUST provide an interface that receives a media type (string inputMediaType) and input data (byte sequence or map inputData)", 
                function() {
                this.skip('TBD');
            });
            it("03 A securing mechanism specification that creates a new type of embedded proof MUST specify a property that relates the verifiable credential or verifiable presentation to a proof graph", 
                function() {
                this.skip('TBD');
            });
            it("04 The securing mechanism MUST define all terms used by the proof graph", 
                function() {
                this.skip('TBD');
            });
            it("05 The securing mechanism MUST secure all graphs in the verifiable credential or the verifiable presentation, except for any proof graphs securing the verifiable credential or the verifiable presentation itself.", 
                function() {
                this.skip('TBD');
            });
        });
    });
    describe("03 Syntaxes", 
        function() { 
        describe("00 Json ld", 
            function() { 
            it("00 JSON-LD compacted document form MUST be utilized for all representations of the data model using the application/vc or application/vp media type.", 
                function() {
                this.skip('TBD');
            });
        });
    });
    describe("04 Algorithms", 
        function() { 
        describe("00 Verification", 
            function() { 
            it("00 This section contains an algorithm that conforming verifier implementations MUST run when verifying a verifiable credential or a verifiable presentation", 
                function() {
                this.skip('TBD');
            });
            it("01 The verifyProof function MUST implement the interface described in 5.13 Securing Mechanism Specifications.", 
                function() {
                this.skip('TBD');
            });
        });
        describe("01 Problem details", 
            function() { 
            it("00 The type property MUST be present and its value MUST be a URL identifying the type of problem.", 
                function() {
                this.skip('TBD');
            });
            it("01 If present, its value MUST be an integer that identifies the type of the problem", 
                function() {
                this.skip('TBD');
            });
            it("02 The title property MUST be present and its value SHOULD provide a short but specific human-readable string for the problem.", 
                function() {
                this.skip('TBD');
            });
            it("03 The detail property MUST be present and its value SHOULD provide a longer human-readable string for the problem.", 
                function() {
                this.skip('TBD');
            });
        });
    });
    describe("05 Internationalization considerations", 
        function() { 
        describe("00 Language and base direction", 
            function() { 
            it("00 When the language value object is used in place of a string value, the object MUST contain a @value property whose value is a string, and SHOULD contain a @language property whose value is a string containing a well-formed Language-Tag as defined by [BCP47], and MAY contain a @direction property whose value is a base direction string defined by the @direction property in [JSON-LD11]", 
                function() {
                this.skip('TBD');
            });
            it("01 The language value object MUST NOT include any other keys beyond @value, @language, and @direction.", 
                function() {
                this.skip('TBD');
            });
        });
    });
    describe("06 Contexts vocabularies types and credential schemas", 
        function() { 
        describe("00 Base context", 
            function() { 
            it("00 Implementations MUST treat the base context value, located at https://www.w3.org/ns/credentials/v2, as already retrieved; the following value is the hexadecimal encoded SHA2-256 digest value of the base context file: 24a18c90e9856d526111f29376e302d970b2bd10182e33959995b0207d7043b9", 
                function() {
                this.skip('TBD');
            });
            it("01 If such operations are performed and result in an error, the verifiable credential or verifiable presentation MUST result in a verification failure.", 
                function() {
                this.skip('TBD');
            });
        });
        describe("01 Vocabularies", 
            function() { 
            it("00 Implementations that depend on RDF vocabulary processing MUST ensure that the following vocabulary URLs used in the base context ultimately resolve to the following files when loading the JSON-LD serializations, which are normative", 
                function() {
                this.skip('TBD');
            });
        });
    });
});