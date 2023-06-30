from manim import *

MathTex.set_default(color=BLACK)
MathTex.set_default(font_size = 30)


## Metrics

induced_metric_brane = MathTex("ds^{2} &= -N^{2} d \\tau^{2} + a^{2} d\\Omega_{3}^{2}")
ads_metric = MathTex("ds^{2}","=","-(1+ k_{\\pm}^{2} r^{2}) dt^{2}", "+", "(1+ k_{\\pm}^{2} r^{2})^{-1} dr^{2}", "+ r^{2} d\Omega_{3}^{2}")
ads_sch_metric = MathTex("ds^{2}","=","-(1+ k_{\\pm}^{2} r^{2} - \\tfrac{8 G_{5} M_{\\pm}}{3 \\pi r^{2}}) dt^{2}", "+", "(1+ k_{\\pm}^{2} r^{2} - \\tfrac{8 G_{5} M_{\\pm}}{3 \\pi r^{2}})^{-1} dr^{2}", "+ r^{2} d\Omega_{3}^{2}")
adS_sch_strings = MathTex("ds^{2}","=","-(1+ k_{\\pm}^{2} r^{2} - \\tfrac{2 G_{5} \\alpha_{\pm}}{r}) dt^{2}", "+", "(1+ k_{\\pm}^{2} r^{2} - \\tfrac{2 G_{5} \\alpha_{\pm}}{r})^{-1} dr^{2}", "+ r^{2} d\Omega_{3}^{2}")
ads_sch_gw = MathTex("ds^{2}","=","-(1+ k_{\\pm}^{2} r^{2}) dt^{2}", "+", "(1+ k_{\\pm}^{2} r^{2})^{-1} dr^{2}", "+ r^{2} d\Omega_{3}^{2}","+","\\zeta^{2}","f(q_{i})\\left(dt^{2}+ dr^{2}\\right)")

## Classical Cosmo eqs

friedmann_induced = MathTex("\\left(\\frac{\\dot{a}}{a}\\right)^{2}","=", "-\\frac{1}{a^{2}}","+", "\\frac{8 \\pi}{3}","2  \\left(\\frac{1}{k_{-}}-\\frac{1}{k_{+}}\\right)^{-1} G_{5}"," \\left(\\sigma_{cr}- \\sigma\\right)","+ \\mathcal{O}(\\epsilon^{2})")
friedmann_usual= MathTex("\\left(\\frac{\\dot{a}}{a}\\right)^{2}","=", "-\\frac{1}{a^{2}}","+", "\\frac{8 \\pi}{3}","G_{4}"," \\Lambda_{4}","+ \\mathcal{O}(\\epsilon^{2})")
friedmann_matter= MathTex("\\left(\\frac{\\dot{a}}{a}\\right)^{2}","=", "-\\frac{1}{a^{2}}","+", "\\frac{8 \\pi}{3}","G_{4}"," \\left(\\Lambda_{4}","+","\\frac{1}{2 \\pi^{2}}\\left(\\tfrac{M_{+}}{k_{+}}- \\tfrac{M_{-}}{k_{-}}\\right)\\frac{1}{a^{4}}\\right)")
friedmann_strings= MathTex("\\left(\\frac{\\dot{a}}{a}\\right)^{2}","=", "-\\frac{1}{a^{2}}","+", "\\frac{8 \\pi}{3}","G_{4}"," \left(\\Lambda_{4}","+","\\frac{3}{8 \\pi a^{3}}\\left(\\tfrac{\\alpha_{+}}{k_{+}}- \\tfrac{\\alpha_{-}}{k_{-}}\\right) \\right)")
friedmann_gw= MathTex("\\left(\\frac{a'(\\eta)}{a(\\eta)}\\right)^{2}","=", "-\\frac{1}{a^{2}}","+", "\\frac{8 \\pi}{3}","G_{4}"," \\left(\\Lambda_{4}","+","3 \\zeta^{2}\\left(\\frac{q_{1}}{a^{2}}- \\frac{q_{3}}{H^{2}a^{4}}\\right) \\right)")

## Actions

bubble_action_5d = MathTex("\\mathcal{S}=","\\frac{1}{2 \\kappa_{5}} \\int d^{5} x \\sqrt{|g|}\\left(R^{(5)}-2 \\Lambda_{5}\\right)","-","\\sigma \\int d^{4} \\zeta \\sqrt{|\\eta|}","+","\\frac{1}{\\kappa_{5}} \\oint d^{4} x \\sqrt{|h|} K ")
hamiltonian_quantum_5d= MathTex("\\mathcal{H} \\psi_{5D}=","\\left(\\left(-\\frac{1}{24 \\pi^{2}}\\frac{1}{a^{3 / 2}} \\frac{d^{2}}{d a^{2}}\\right)+6 \\pi^{2} V(a)\\right)","a^{3 / 2} \\psi_{5D}","=0")

## Junctions

junctions = MathTex(r' h_{ab}^{(+)} &= h_{ab}^{(-)}\\ S_{ab} &= \kappa_{5}^{-1}\left([K_{ab}^{(+)} \pm K_{ab}^{(-)}]-[K^{(+)} \pm K^{(-)}]h_{ab}\right)')
junctions_our_model = MathTex(r'S_{ab} &= \kappa_{5}^{-1}\left([K_{ab}^{(+)} - K_{ab}^{(-)}]-[K^{(+)} - K^{(-)}]h_{ab}\right)')
critical_tension_rs= MathTex(r' \sigma = \frac{3 \left(k + k\right)}{\kappa_{5}}')
critical_tension_db= MathTex(r' \sigma_{cr} = \frac{3}{\kappa_{5}}\left(k_{-}-k_{+}\right)')
brane_tension_db= MathTex(r'\sigma &= \frac{3}{\kappa^{2}_{5}} \left(\sqrt{k_{-}^{2} + \frac{1+ \dot{a}^{2}}{a^{2}}} -\sqrt{k_{+}^{2} + \frac{1+ \dot{a}^{2}}{a^{2}}} \right)')

## Quantum

wheeler_de_witt= MathTex("\\mathcal{H} \\psi(a)= \\frac{N}{a} \\left(-\\frac{1}{24 \\pi^{2}} \\frac{d^{2}}{da^{2}} + 6 \\pi^{2}", "\\left(a^{2} -\\frac{a^{4}}{a_{0}^{2}}\\right)","\\right)\\psi(a)= 0")
wkbwavespsi= MathTex(r'\Psi(a) =')
wkbwaves0= MathTex(r' \left\{',font_size=70).next_to(wkbwavespsi, RIGHT)
wkbwaves1= MathTex(r'a \:e^{S(a_{0},0)} + b\: e^{-S(a_{0},0)},& \quad a \leq a_{0} \\c \:e^{i\:S(a,a_{0})} + d\: e^{-i\: S(a,a_{0})}, & \quad a \geq a_{0}').next_to(wkbwaves0, RIGHT)
wkbwaves= VGroup(wkbwavespsi,wkbwaves0,wkbwaves1)
weights= MathTex("P_{HH} \propto e^{+2 S_{0}}","P_{V} \propto e^{-2 S_{0}}")
nucprobBT= MathTex("P \propto e^{-B}", "=e^","{ \\frac{-8 \\pi^{2} a_{0}^{2}}{\\kappa_{4}}}")
nucprobWKB= MathTex("P \propto e^{-2 \\int p d\\tau}","=e^","{\\frac{-8 \\pi^{2} a_{0}^{2}}{\\kappa_{4}}}")




