# library untuk membuat grafik dari data yang ditampilkan 
import matplotlib.pyplot as plt

'''Line Chart Module'''

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
nilai = [12,34,56,78,90]
ax.plot(nilai)

plt.show()      # menampilkan 


'''Bar Chart'''

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
MataKuliah = ['Matematika', 'Fisika', 'Kimia', 'Komputer', 'Bahasa']
Nilai = [80,90,65,79,82]
ax.bar(MataKuliah,Nilai)
plt.show()

'''Pie Chart'''

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
MataKuliah = ['Matematika', 'Fisika', 'Kimia', 'Komputer', 'Bahasa']
Nilai = [80,90,65,79,82]
ax.pie(Nilai,labels=MataKuliah,autopct='%1.2f%%')
plt.show()


'''Scatter plot'''
 
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
tugas = [80,90,65,79,82]
uts = [70,80,85,59,92]
uas = [82,92,87,77,84]

# hubungan tugas dengan uts
ax.scatter(tugas,uts,color='red')
# hubungan tugas dengan uas
ax.scatter(tugas,uas,color='blue')

# set label X dan Y
ax.set_xlabel('Tugas')
ax.set_ylabel('Nilai')
ax.set_title('Scatter Plot')