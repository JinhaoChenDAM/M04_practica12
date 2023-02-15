import xml.etree.ElementTree as ET


# Creates an XML with students info and prints it out
def createXML():
    # creates a root with students
    root = ET.Element("students")
    names = ["Jinhao", "Guillermo", "Federico", "Jack", "Jhon"]
    surnames = ["Chen", "Jaume", "Fuentes", "Sparrow", "Casanovas"]
    emails = ["jinhaochen@gmail.com", "guillermojaume@gmail.com", "federicofuentes@gmail.com", "jacksparrow@gmail.com",
              "jhoncasanovas@gmail.com"]
    dnis = ["123456789", "213431231", "323456456", "234231456", "234123445"]
    # creates 5 students with an attribute and name, surname, email and dni subtags
    for i in range(5):
        student = ET.SubElement(root, 'student')
        student.set('type', 'Games')
        name = ET.SubElement(student, 'name')
        name.text = names[i]
        surname = ET.SubElement(student, 'surname')
        surname.text = surnames[i]
        email = ET.SubElement(student, 'email')
        email.text = emails[i]
        dni = ET.SubElement(student, 'dni')
        dni.text = dnis[i]
    # indent the elements
    ET.indent(root)
    # prints the tree
    ET.dump(root)
    tree = ET.ElementTree(root)
    # creates the file
    tree.write("arxiu.xml")
