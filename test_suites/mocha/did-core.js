describe("Decentralized Identifiers (DIDs) v1.0", 
    function() { 
    describe("00 Introduction", 
        function() { 
        describe("00 Conformance", 
            function() { 
            it("00 The key words MAY, MUST, MUST NOT, OPTIONAL, RECOMMENDED, REQUIRED, SHOULD, and SHOULD NOT in this document are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all capitals, as shown here.", 
                function() {
                this.skip('TBD');
            });
        });
    });
    describe("01 Identifier", 
        function() { 
        describe("00 Did syntax", 
            function() { 
            it("00 All DIDs MUST conform to the DID Syntax ABNF Rules.", 
                function() {
                this.skip('TBD');
            });
        });
        describe("01 Did url syntax", 
            function() { 
            it("00 All DID URLs MUST conform to the DID URL Syntax ABNF Rules", 
                function() {
                this.skip('TBD');
            });
            it("01 If present, the associated value MUST be an ASCII string.", 
                function() {
                this.skip('TBD');
            });
            it("02 If present, the associated value MUST be an ASCII string and MUST use percent-encoding for certain characters as specified in RFC3986 Section 2.1.", 
                function() {
                this.skip('TBD');
            });
            it("03 If present, the associated value MUST be an ASCII string which is a valid XML datetime value, as defined in section 3.3.7 of W3C XML Schema Definition Language (XSD) 1.1 Part 2: Datatypes [XMLSCHEMA11-2]", 
                function() {
                this.skip('TBD');
            });
            it("04 This datetime value MUST be normalized to UTC 00:00:00 and without sub-second decimal precision", 
                function() {
                this.skip('TBD');
            });
            it("05 When resolving a relative DID URL reference, the algorithm specified in RFC3986 Section 5: Reference Resolution MUST be used", 
                function() {
                this.skip('TBD');
            });
        });
    });
    describe("02 Core properties", 
        function() { 
        describe("00 Identifiers", 
            function() { 
            it("00 The value of id MUST be a string that conforms to the rules in 3.1 DID Syntax and MUST exist in the root map of the data model for the DID document.", 
                function() {
                this.skip('TBD');
            });
            it("01 If present, the value MUST be a string or a set of strings that conform to the rules in 3.1 DID Syntax", 
                function() {
                this.skip('TBD');
            });
            it("02 If present, the value MUST be a set where each item in the set is a URI conforming to [RFC3986].", 
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
            it("01 The verification method map MUST include the id, type, controller, and specific verification material properties that are determined by the value of type and are defined in 5.2.1 Verification Material", 
                function() {
                this.skip('TBD');
            });
            it("02 The value of the id property for a verification method MUST be a string that conforms to the rules in Section 3.2 DID URL Syntax.", 
                function() {
                this.skip('TBD');
            });
            it("03 The value of the type property MUST be a string that references exactly one verification method type", 
                function() {
                this.skip('TBD');
            });
            it("04 The value of the controller property MUST be a string that conforms to the rules in 3.1 DID Syntax.", 
                function() {
                this.skip('TBD');
            });
            it("05 If present, the value MUST be a map representing a JSON Web Key that conforms to [RFC7517]", 
                function() {
                this.skip('TBD');
            });
            it("06 The map MUST NOT contain 'd', or any other members of the private information class as described in Registration Template", 
                function() {
                this.skip('TBD');
            });
            it("07 If present, the value MUST be a string representation of a [MULTIBASE] encoded public key.", 
                function() {
                this.skip('TBD');
            });
            it("08 A verification method MUST NOT contain multiple verification material properties for the same material", 
                function() {
                this.skip('TBD');
            });
        });
        describe("02 Verification relationships", 
            function() { 
            it("00 If present, the associated value MUST be a set of one or more verification methods", 
                function() {
                this.skip('TBD');
            });
        });
        describe("03 Services", 
            function() { 
            it("00 If present, the associated value MUST be a set of services, where each service is described by a map", 
                function() {
                this.skip('TBD');
            });
            it("01 Each service map MUST contain id, type, and serviceEndpoint properties", 
                function() {
                this.skip('TBD');
            });
            it("02 The value of the id property MUST be a URI conforming to [RFC3986]", 
                function() {
                this.skip('TBD');
            });
            it("03 A conforming producer MUST NOT produce multiple service entries with the same id", 
                function() {
                this.skip('TBD');
            });
            it("04 A conforming consumer MUST produce an error if it detects multiple service entries with the same id.", 
                function() {
                this.skip('TBD');
            });
            it("05 The value of the type property MUST be a string or a set of strings", 
                function() {
                this.skip('TBD');
            });
            it("06 The value of the serviceEndpoint property MUST be a string, a map, or a set composed of one or more strings and/or maps", 
                function() {
                this.skip('TBD');
            });
            it("07 All string values MUST be valid URIs conforming to [RFC3986] and normalized according to the Normalization and Comparison rules in RFC3986 and to any normalization rules in its applicable URI scheme specification.", 
                function() {
                this.skip('TBD');
            });
        });
    });
    describe("03 Representations", 
        function() { 
        describe("00 Production and consumption", 
            function() { 
            it("00 A representation MUST define deterministic production and consumption rules for all data types specified in 4", 
                function() {
                this.skip('TBD');
            });
            it("01 A representation MUST be uniquely associated with an IANA-registered Media Type.", 
                function() {
                this.skip('TBD');
            });
            it("02 A representation MUST define fragment processing rules for its Media Type that are conformant with the fragment processing rules defined in Fragment.", 
                function() {
                this.skip('TBD');
            });
            it("03 A conforming producer MUST take a DID document data model and a representation-specific entries map as input into the production process", 
                function() {
                this.skip('TBD');
            });
            it("04 A conforming producer MUST serialize all entries in the DID document data model, and the representation-specific entries map, that do not have explicit processing rules for the representation being produced using only the representation's data type processing rules and return the serialization after the production process completes.", 
                function() {
                this.skip('TBD');
            });
            it("05 A conforming producer MUST return the Media Type string associated with the representation after the production process completes.", 
                function() {
                this.skip('TBD');
            });
            it("06 A conforming producer MUST NOT produce non-conforming DIDs or DID documents.", 
                function() {
                this.skip('TBD');
            });
            it("07 A conforming consumer MUST take a representation and Media Type string as input into the consumption process", 
                function() {
                this.skip('TBD');
            });
            it("08 A conforming consumer MUST determine the representation of a DID document using the Media Type input string.", 
                function() {
                this.skip('TBD');
            });
            it("09 A conforming consumer MUST detect any representation-specific entry across all known representations and place the entry into a representation-specific entries map which is returned after the consumption process completes", 
                function() {
                this.skip('TBD');
            });
            it("10 A conforming consumer MUST add all non-representation-specific entries that do not have explicit processing rules for the representation being consumed to the DID document data model using only the representation's data type processing rules and return the DID document data model after the consumption process completes.", 
                function() {
                this.skip('TBD');
            });
            it("11 A conforming consumer MUST produce errors when consuming non-conforming DIDs or DID documents.", 
                function() {
                this.skip('TBD');
            });
        });
        describe("01 Json", 
            function() { 
            it("00 The DID document, DID document data structures, and representation-specific entries map MUST be serialized to the JSON representation according to the following production rules:", 
                function() {
                this.skip('TBD');
            });
            it("01 All entries of a DID document MUST be included in the root JSON Object", 
                function() {
                this.skip('TBD');
            });
            it("02 When serializing a DID document, a conforming producer MUST specify a media type of application/did+json to downstream applications such as described in 7.1.2 DID Resolution Metadata.", 
                function() {
                this.skip('TBD');
            });
            it("03 The DID document and DID document data structures JSON representation MUST be deserialized into the data model according to the following consumption rules:", 
                function() {
                this.skip('TBD');
            });
            it("04 If media type information is available to a conforming consumer and the media type value is application/did+json, then the data structure being consumed is a DID document, and the root element MUST be a JSON Object where all members of the object are entries of the DID document", 
                function() {
                this.skip('TBD');
            });
            it("05 A conforming consumer for a JSON representation that is consuming a DID document with a root element that is not a JSON Object MUST report an error.", 
                function() {
                this.skip('TBD');
            });
        });
        describe("02 Json ld", 
            function() { 
            it("00 The DID document, DID document data structures, and representation-specific entries map MUST be serialized to the JSON-LD representation according to the JSON representation production rules as defined in 6.2 JSON.", 
                function() {
                this.skip('TBD');
            });
            it("01 In addition to using the JSON representation production rules, JSON-LD production MUST include the representation-specific @context entry", 
                function() {
                this.skip('TBD');
            });
            it("02 The serialized value of @context MUST be the JSON String https://www.w3.org/ns/did/v1, or a JSON Array where the first item is the JSON String https://www.w3.org/ns/did/v1 and the subsequent items are serialized according to the JSON representation production rules.", 
                function() {
                this.skip('TBD');
            });
            it("03 When serializing a JSON-LD representation of a DID document, a conforming producer MUST specify a media type of application/did+ld+json to downstream applications such as described in 7.1.2 DID Resolution Metadata.", 
                function() {
                this.skip('TBD');
            });
            it("04 The DID document and any DID document data structures expressed by a JSON-LD representation MUST be deserialized into the data model according to the JSON representation consumption rules as defined in 6.2 JSON.", 
                function() {
                this.skip('TBD');
            });
        });
    });
    describe("04 Resolution", 
        function() { 
        describe("00 Did resolution", 
            function() { 
            it("00 This input is REQUIRED and the value MUST be a conformant DID as defined in 3.1 DID Syntax.", 
                function() {
                this.skip('TBD');
            });
            it("01 This input is REQUIRED, but the structure MAY be empty.", 
                function() {
                this.skip('TBD');
            });
            it("02 This structure is REQUIRED, and in the case of an error in the resolution process, this MUST NOT be empty", 
                function() {
                this.skip('TBD');
            });
            it("03 If resolveRepresentation was called, this structure MUST contain a contentType property containing the Media Type of the representation found in the didDocumentStream", 
                function() {
                this.skip('TBD');
            });
            it("04 If the resolution is not successful, this structure MUST contain an error property describing the error.", 
                function() {
                this.skip('TBD');
            });
            it("05 If the resolution is successful, and if the resolve function was called, this MUST be a DID document abstract data model (a map) as described in 4", 
                function() {
                this.skip('TBD');
            });
            it("06 The value of id in the resolved DID document MUST match the DID that was resolved", 
                function() {
                this.skip('TBD');
            });
            it("07 If the resolution is unsuccessful, this value MUST be empty.", 
                function() {
                this.skip('TBD');
            });
            it("08 If the resolution is successful, and if the resolveRepresentation function was called, this MUST be a byte stream of the resolved DID document in one of the conformant representations", 
                function() {
                this.skip('TBD');
            });
            it("09 If the resolution is unsuccessful, this value MUST be an empty stream.", 
                function() {
                this.skip('TBD');
            });
            it("10 If the resolution is successful, this MUST be a metadata structure", 
                function() {
                this.skip('TBD');
            });
            it("11 If the resolution is unsuccessful, this output MUST be an empty metadata structure", 
                function() {
                this.skip('TBD');
            });
            it("12 The Media Type MUST be expressed as an ASCII string", 
                function() {
                this.skip('TBD');
            });
            it("13 This property is OPTIONAL for the resolveRepresentation function and MUST NOT be used with the resolve function.", 
                function() {
                this.skip('TBD');
            });
            it("14 This property is REQUIRED if resolution is successful and if the resolveRepresentation function was called", 
                function() {
                this.skip('TBD');
            });
            it("15 This property MUST NOT be present if the resolve function was called", 
                function() {
                this.skip('TBD');
            });
            it("16 The value of this property MUST be an ASCII string that is the Media Type of the conformant representations", 
                function() {
                this.skip('TBD');
            });
            it("17 The caller of the resolveRepresentation function MUST use this value when determining how to parse and process the didDocumentStream returned by this function into the data model.", 
                function() {
                this.skip('TBD');
            });
            it("18 This property is REQUIRED when there is an error in the resolution process", 
                function() {
                this.skip('TBD');
            });
            it("19 The value of this property MUST be a single keyword ASCII string", 
                function() {
                this.skip('TBD');
            });
            it("20 The value of the property MUST be a string formatted as an XML Datetime normalized to UTC 00:00:00 and without sub-second decimal precision", 
                function() {
                this.skip('TBD');
            });
            it("21 The value of the property MUST follow the same formatting rules as the created property", 
                function() {
                this.skip('TBD');
            });
            it("22 If a DID has been deactivated, DID document metadata MUST include this property with the boolean value true", 
                function() {
                this.skip('TBD');
            });
            it("23 If a DID has not been deactivated, this property is OPTIONAL, but if included, MUST have the boolean value false.", 
                function() {
                this.skip('TBD');
            });
            it("24 The value of the property MUST follow the same formatting rules as the created property.", 
                function() {
                this.skip('TBD');
            });
            it("25 The value of the property MUST be an ASCII string.", 
                function() {
                this.skip('TBD');
            });
            it("26 If present, the value MUST be a set where each item is a string that conforms to the rules in Section 3.1 DID Syntax", 
                function() {
                this.skip('TBD');
            });
            it("27 Each equivalentId DID value MUST be produced by, and a form of, the same DID method as the id property value", 
                function() {
                this.skip('TBD');
            });
            it("28 A conforming DID method specification MUST guarantee that each equivalentId value is logically equivalent to the id property value.", 
                function() {
                this.skip('TBD');
            });
            it("29 equivalentId is a much stronger form of equivalence than alsoKnownAs because the equivalence MUST be guaranteed by the governing DID method", 
                function() {
                this.skip('TBD');
            });
            it("30 If present, the value MUST be a string that conforms to the rules in Section 3.1 DID Syntax", 
                function() {
                this.skip('TBD');
            });
            it("31 A canonicalId value MUST be produced by, and a form of, the same DID method as the id property value", 
                function() {
                this.skip('TBD');
            });
            it("32 A conforming DID method specification MUST guarantee that the canonicalId value is logically equivalent to the id property value.", 
                function() {
                this.skip('TBD');
            });
        });
        describe("01 Did url dereferencing", 
            function() { 
            it("00 To dereference a DID fragment, the complete DID URL including the DID fragment MUST be used", 
                function() {
                this.skip('TBD');
            });
            it("01 This input is REQUIRED", 
                function() {
                this.skip('TBD');
            });
            it("02 This input is REQUIRED, but the structure MAY be empty.", 
                function() {
                this.skip('TBD');
            });
            it("03 This structure is REQUIRED, and in the case of an error in the dereferencing process, this MUST NOT be empty", 
                function() {
                this.skip('TBD');
            });
            it("04 If the dereferencing is not successful, this structure MUST contain an error property describing the error.", 
                function() {
                this.skip('TBD');
            });
            it("05 If the dereferencing function was called and successful, this MUST contain a resource corresponding to the DID URL", 
                function() {
                this.skip('TBD');
            });
            it("06 If the dereferencing is unsuccessful, this value MUST be empty.", 
                function() {
                this.skip('TBD');
            });
            it("07 If the dereferencing is successful, this MUST be a metadata structure, but the structure MAY be empty", 
                function() {
                this.skip('TBD');
            });
            it("08 If the contentStream is a DID document, this MUST be a didDocumentMetadata structure as described in DID Resolution", 
                function() {
                this.skip('TBD');
            });
            it("09 If the dereferencing is unsuccessful, this output MUST be an empty metadata structure.", 
                function() {
                this.skip('TBD');
            });
            it("10 The Media Type MUST be expressed as an ASCII string", 
                function() {
                this.skip('TBD');
            });
            it("11 The Media Type value MUST be expressed as an ASCII string.", 
                function() {
                this.skip('TBD');
            });
            it("12 This property is REQUIRED when there is an error in the dereferencing process", 
                function() {
                this.skip('TBD');
            });
            it("13 The value of this property MUST be a single keyword expressed as an ASCII string", 
                function() {
                this.skip('TBD');
            });
        });
        describe("02 Metadata structure", 
            function() { 
            it("00 The structure used to communicate this metadata MUST be a map of properties", 
                function() {
                this.skip('TBD');
            });
            it("01 Each property name MUST be a string", 
                function() {
                this.skip('TBD');
            });
            it("02 Each property value MUST be a string, map, list, set, boolean, or null", 
                function() {
                this.skip('TBD');
            });
            it("03 The values within any complex data structures such as maps and lists MUST be one of these data types as well", 
                function() {
                this.skip('TBD');
            });
            it("04 All metadata property definitions registered in the DID Specification Registries [DID-SPEC-REGISTRIES] MUST define the value type, including any additional formats or restrictions to that value (for example, a string formatted as a date or as a decimal integer)", 
                function() {
                this.skip('TBD');
            });
            it("05 The entire metadata structure MUST be serializable according to the JSON serialization rules in the [INFRA] specification", 
                function() {
                this.skip('TBD');
            });
        });
    });
    describe("05 Methods", 
        function() { 
        describe("00 Method syntax", 
            function() { 
            it("00 A DID method specification MUST define exactly one method-specific DID scheme that is identified by exactly one method name as specified by the method-name rule in 3.1 DID Syntax.", 
                function() {
                this.skip('TBD');
            });
            it("01 The DID method specification MUST specify how to generate the method-specific-id component of a DID.", 
                function() {
                this.skip('TBD');
            });
            it("02 The DID method specification MUST define sensitivity and normalization of the value of the method-specific-id.", 
                function() {
                this.skip('TBD');
            });
            it("03 The method-specific-id value MUST be unique within a DID method", 
                function() {
                this.skip('TBD');
            });
            it("04 Any DID generated by a DID method MUST be globally unique.", 
                function() {
                this.skip('TBD');
            });
            it("05 The use of colons MUST comply syntactically with the method-specific-id ABNF rule.", 
                function() {
                this.skip('TBD');
            });
        });
        describe("01 Method operations", 
            function() { 
            it("00 A DID method specification MUST define how authorization is performed to execute all operations, including any necessary cryptographic processes.", 
                function() {
                this.skip('TBD');
            });
            it("01 A DID method specification MUST specify how a DID controller creates a DID and its associated DID document.", 
                function() {
                this.skip('TBD');
            });
            it("02 A DID method specification MUST specify how a DID resolver uses a DID to resolve a DID document, including how the DID resolver can verify the authenticity of the response.", 
                function() {
                this.skip('TBD');
            });
            it("03 A DID method specification MUST specify what constitutes an update to a DID document and how a DID controller can update a DID document or state that updates are not possible.", 
                function() {
                this.skip('TBD');
            });
            it("04 The DID method specification MUST specify how a DID controller can deactivate a DID or state that deactivation is not possible.", 
                function() {
                this.skip('TBD');
            });
        });
        describe("02 Security requirements", 
            function() { 
            it("00 A DID method specifications MUST follow all guidelines and normative language provided in RFC3552: Writing Security Considerations Sections for the DID operations defined in the DID method specification.", 
                function() {
                this.skip('TBD');
            });
            it("01 The Security Considerations section MUST document the following forms of attack for the DID operations defined in the DID method specification: eavesdropping, replay, message insertion, deletion, modification, denial of service, amplification, and man-in-the-middle", 
                function() {
                this.skip('TBD');
            });
            it("02 The Security Considerations section MUST discuss residual risks, such as the risks from compromise in a related protocol, incorrect implementation, or cipher after threat mitigation was deployed.", 
                function() {
                this.skip('TBD');
            });
            it("03 The Security Considerations section MUST provide integrity protection and update authentication for all operations required by Section 8.2 Method Operations.", 
                function() {
                this.skip('TBD');
            });
            it("04 If authentication is involved, particularly user-host authentication, the security characteristics of the authentication method MUST be clearly documented.", 
                function() {
                this.skip('TBD');
            });
            it("05 The Security Considerations section MUST discuss the policy mechanism by which DIDs are proven to be uniquely assigned.", 
                function() {
                this.skip('TBD');
            });
            it("06 Method-specific endpoint authentication MUST be discussed", 
                function() {
                this.skip('TBD');
            });
            it("07 Where DID methods make use of DLTs with varying network topology, sometimes offered as light node or thin client implementations to reduce required computing resources, the security assumptions of the topology available to implementations of the DID method MUST be discussed.", 
                function() {
                this.skip('TBD');
            });
            it("08 If a protocol incorporates cryptographic protection mechanisms, the DID method specification MUST clearly indicate which portions of the data are protected and by what protections, and it SHOULD give an indication of the sorts of attacks to which the cryptographic protection is susceptible", 
                function() {
                this.skip('TBD');
            });
        });
        describe("03 Privacy requirements", 
            function() { 
            it("00 The DID method specification's Privacy Considerations section MUST discuss any subsection of Section 5 of [RFC6973] that could apply in a method-specific manner", 
                function() {
                this.skip('TBD');
            });
        });
    });
});