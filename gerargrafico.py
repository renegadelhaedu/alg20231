#pip install matplotlib
import matplotlib.pyplot as plt

# creating the dataset
data = {'Mesa': 20, 'Cadeira': 15, 'Corda': 30,
        'COrtina': 35}
courses = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize=(10, 5))

# creating the bar plot
plt.bar(courses, values, color='maroon',
        width=0.4)

plt.xlabel("Produtos")
plt.ylabel("Quantidade")
plt.title("Sertao Livre")
plt.show()