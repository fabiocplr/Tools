import xml.etree.ElementTree as ET

# Pfad zur XML-Datei (ändere diesen Pfad entsprechend)
file_path = "Pfad/zur/Datei/Masterarbeit_Test1_GermanOnly.xml"

# Namespace-Deklarationen aus der Datei
namespaces = {
    "ns3": "http://www.schema.de/2004/ST4/XmlImportExport/Node"
}

# XML-Datei laden
tree = ET.parse(file_path)
root = tree.getroot()

# Liste zur Speicherung der Zeichenanzahl
content_lengths = []

# Alle deutschen <content>-Blöcke durchsuchen und ihre <p>-Tags extrahieren
for value in root.findall(".//ns3:Value[@ns3:Aspect='de']", namespaces):
    for entry in value.findall(".//ns3:Entry", namespaces):
        content_element = entry.find(".//content", namespaces)
        if content_element is not None:
            # Suche nach <p>-Tags innerhalb des <content>-Elements
            paragraphs = content_element.findall(".//p", namespaces)
            paragraph_texts = [p.text.strip() for p in paragraphs if p.text]
            
            # Berechnung der Zeichenanzahl der kombinierten Absätze
            if paragraph_texts:
                total_length = sum(len(text) for text in paragraph_texts)
                content_lengths.append(total_length)

# Durchschnittliche Zeichenanzahl berechnen
if content_lengths:
    average_length = sum(content_lengths) / len(content_lengths)
    max_length = max(content_lengths)
    min_length = min(content_lengths)
else:
    average_length = max_length = min_length = 0

# Ergebnisse ausgeben
print(f"Durchschnittliche Zeichenanzahl pro Content-Block: {average_length:.2f}")
print(f"Maximale Zeichenanzahl: {max_length}")
print(f"Minimale Zeichenanzahl: {min_length}")
print(f"Anzahl der Content-Blöcke: {len(content_lengths)}")
