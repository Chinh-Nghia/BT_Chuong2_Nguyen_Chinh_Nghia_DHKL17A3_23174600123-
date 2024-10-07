from xml.dom import minidom

# Tải và phân tích file XML
file = 'sample.xml'
doc = minidom.parse(file)

# Lấy tên công ty
company_name = doc.getElementsByTagName("name")[0].firstChild.data
print(f"Company Name: {company_name}")

# Lấy phiên bản
version = doc.getElementsByTagName("version")[0].firstChild.data
print(f"Version: {version}")

# Lấy thông tin của các nhân viên
staffs = doc.getElementsByTagName("staff")

for staff in staffs:
    staff_id = staff.getAttribute("id")
    name = staff.getElementsByTagName("name")[0].firstChild.data
    salary = staff.getElementsByTagName("salary")[0].firstChild.data
    print(f"Staff ID: {staff_id}")
    print(f"Name: {name}")
    print(f"Salary: {salary}")
    print("-" * 20)
