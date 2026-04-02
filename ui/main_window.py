
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from solver.material_db import materials
from solver.fem_beam import solve_beam, compute_stress
from solver.optimizer import optimize
from postprocessing.stress_plot import plot_stress
from postprocessing.report_generator import generate

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AeroStructPy Elite")

        main=QHBoxLayout()

        side=QVBoxLayout()
        self.mat=QComboBox(); self.mat.addItems(materials.keys())
        self.solve_btn=QPushButton("Solve")

        side.addWidget(QLabel("Material")); side.addWidget(self.mat)
        side.addWidget(self.solve_btn)

        self.tabs=QTabWidget()

        g=QWidget(); gl=QVBoxLayout()
        self.L=QLineEdit(); self.L.setPlaceholderText("Length")
        self.n=QLineEdit(); self.n.setPlaceholderText("Elements")
        gl.addWidget(self.L); gl.addWidget(self.n); g.setLayout(gl)

        l=QWidget(); ll=QVBoxLayout()
        self.load=QLineEdit(); self.load.setPlaceholderText("Load")
        self.slider=QSlider(Qt.Orientation.Horizontal)
        self.slider.setMinimum(1); self.slider.setMaximum(10000)
        ll.addWidget(self.load); ll.addWidget(self.slider); l.setLayout(ll)

        r=QWidget(); rl=QVBoxLayout()
        self.out=QLabel("Results"); rl.addWidget(self.out); r.setLayout(rl)

        self.tabs.addTab(g,"Geometry")
        self.tabs.addTab(l,"Loads")
        self.tabs.addTab(r,"Results")

        cont=QWidget(); main.addLayout(side,1); main.addWidget(self.tabs,4)
        cont.setLayout(main); self.setCentralWidget(cont)

        self.solve_btn.clicked.connect(self.run)
        self.slider.valueChanged.connect(self.live)

    def live(self):
        self.load.setText(str(self.slider.value()))
        self.run()

    def run(self):
        try:
            mat=self.mat.currentText()
            E=materials[mat]["E"]
            d=materials[mat]
            L=float(self.L.text()); n=int(self.n.text())
            load=float(self.load.text())
            I=1e-6; c=0.01

            u=solve_beam(E,I,L,n,load)
            s=compute_stress(u,E,I,L,n,c)
            plot_stress(s,L)

            opt=optimize(E,d["density"],d["yield"],L,load,n)
            self.out.setText(f"Max def={min(u):.2e}\nOpt I={opt['I']:.2e}")

            generate({"Material":mat,"L":L,"Load":load,"Opt":opt},"stress.png")
        except Exception as e:
            self.out.setText(str(e))
