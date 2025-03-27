# ODBA
**mappingId	Personal Information**

SELECT ID, deptID,uniID, firstName, lastName, email, telephone FROM People

→ SELECT ID, deptID,uniID, firstName, lastName, email, telephone, **role** FROM People


**mappingId	Full Professor**

source		SELECT deptID, uniID, profID, underGradDegreeID, masterDegreeID, doctoralDegreeID, researchInterestID FROM Professors WHERE profType = 'FullProfessor'

→ source		SELECT deptID, uniID, profID, underGradDegreeID, masterDegreeID, doctoralDegreeID, researchInterestID, **profType** FROM Professors WHERE profType = 'FullProfessor'

**mappingId	Associate Professor**

SELECT deptID, uniID, profID, underGradDegreeID, masterDegreeID, doctoralDegreeID, researchInterestID FROM Professors WHERE profType = 'AssociateProfessor'

→ SELECT deptID, uniID, profID, underGradDegreeID, masterDegreeID, doctoralDegreeID, researchInterestID, **profType** FROM Professors WHERE profType = 'AssociateProfessor'

**mappingId	Assistant Professor**

SELECT deptID, uniID, profID, underGradDegreeID, masterDegreeID, doctoralDegreeID, researchInterestID FROM Professors WHERE profType = 'AssistantProfessor'

→ SELECT deptID, uniID, profID, underGradDegreeID, masterDegreeID, doctoralDegreeID, researchInterestID, **profType** FROM Professors WHERE profType = 'AssistantProfessor'

**mappingID Graduate Student**

 :hasMajor {major} .  →  :hasMajor **<{major}>** . 

**mappingId	Undergraduate Student**

:hasMajor {major} . →  :hasMajor **<{major}>** . 

**mappingId	like**

:like {interest} . → :like **<{interest}>** .

**mappingId	isCrazyAbout**

:isCrazyAbout {interest} .  → :isCrazyAbout **<{interest}>** . 

# Ontology
<owl:DatatypeProperty rdf:about="http://uob.iodt.ibm.com/univ-bench-dl.owl#researchInterest">

→ <owl:**ObjectProperty** rdf:about="http://uob.iodt.ibm.com/univ-bench-dl.owl#researchInterest">