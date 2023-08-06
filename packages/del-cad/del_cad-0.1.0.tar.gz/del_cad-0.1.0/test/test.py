import del_cad
import matplotlib.pyplot as plt

if __name__ == "__main__":
    my_class = del_cad.MyClass()
    my_class.add_polygon(
        [0.0, 0.0,
         1.0, 0.0,
        1.0, 1.0])
    tri2vtx, vtx2xy = my_class.triangulation(0.03)
    fig2, ax2 = plt.subplots()
    ax2.set_aspect('equal')
    ax2.triplot(vtx2xy[:,0], vtx2xy[:, 1], tri2vtx)
    plt.show()