from xml.dom import minidom

# Tải và phân tích file XML
file = 'sample.xml'
doc = minidom.parse(file)

# Lấy danh sách tất cả các phần tử
elements = doc.getElementsByTagName('*')  # Dấu '*' để lấy tất cả các phần tử

# In ra tên của từng phần tử
for element in elements:
    print(f"Element Name: {element.tagName}")
