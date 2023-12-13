from manim import *

## Metrics

class EqMetric(MathTex):
    """class as a collection of metric/line invariant equations.

    Parameters:
        - color: no need to explain.
        - size: font_size.
    """
    def __init__(self, my_color, my_font_size, **kwargs):
        super().__init__(**kwargs)

        self.ind_metric_brane = MathTex("ds^{2} &= -N^{2} d \\tau^{2} + a^{2} d\\Omega_{3}^{2}", color = my_color, font_size = my_font_size)
        self.ads_metric = MathTex("ds^{2}","=","-(1+ k_{\\pm}^{2} r^{2}) dt^{2}", "+", "(1+ k_{\\pm}^{2} r^{2})^{-1} dr^{2}", "+ r^{2} d\Omega_{3}^{2}" ,color = my_color, font_size = my_font_size)
        self.ads_sch_metric = MathTex("ds^{2}","=","-(1+ k_{\\pm}^{2} r^{2} - \\tfrac{8 G_{5} M_{\\pm}}{3 \\pi r^{2}}) dt^{2}", "+", "(1+ k_{\\pm}^{2} r^{2} - \\tfrac{8 G_{5} M_{\\pm}}{3 \\pi r^{2}})^{-1} dr^{2}", "+ r^{2} d\Omega_{3}^{2}",color = my_color, font_size = my_font_size)
        self.ads_sch_strings = MathTex("ds^{2}","=","-(1+ k_{\\pm}^{2} r^{2} - \\tfrac{2 G_{5} \\alpha_{\pm}}{r}) dt^{2}", "+", "(1+ k_{\\pm}^{2} r^{2} - \\tfrac{2 G_{5} \\alpha_{\pm}}{r})^{-1} dr^{2}", "+ r^{2} d\Omega_{3}^{2}",color = my_color, font_size = my_font_size)
        self.ads_sch_gw = MathTex("ds^{2}","=","-(1+ k_{\\pm}^{2} r^{2}) dt^{2}", "+", "(1+ k_{\\pm}^{2} r^{2})^{-1} dr^{2}", "+ r^{2} d\Omega_{3}^{2}","+","\\zeta^{2}","f(q_{i})\\left(dt^{2}+ dr^{2}\\right)",color = my_color, font_size = my_font_size)
        self.bh_10d = MathTex("d s_{10}^2","=","-h[r]^{-2} f[r] dt^2+h[r]\\left(f[r]^{-1} d r^2+r^2 d \\Omega_{3}^{2}\\right)","+","L^2 \\sum_{i=1}^{3}\\left\{d \\sigma_i^2+\\sigma_i^2\\left(d \\phi_i+L^{-1} A(r)\\right)^2\\right\}",color = my_color, font_size = my_font_size)
        self.bh_10d_rs = MathTex("d s_{10}^2","=","-g[z]dt^2+g[z]^{-1}dz^2+z^2d \\Omega_3^2","+","L^2 \\sum_{i=1}^3\\left\{d \\sigma_i^2+\\sigma_i^2\\left(d \\phi_i+L^{-1} A(z)\\right)^2\\right\}",color = my_color, font_size = my_font_size)
        self.g_rs= MathTex("g[z]=1+k^2 z^2-\\frac{2 \\kappa_5 \\mu}{z^2}+\\frac{\\kappa_5^2 \\theta^2}{z^4}",color = my_color, font_size = my_font_size)

## Classical Cosmo eqs

class EqCosmo(MathTex):
    """class as a collection of classical cosmology equations.

    Parameters:
        - color: no need to explain.
        - size: font_size.
    """
    def __init__(self,my_color, my_font_size, **kwargs):
        super().__init__(**kwargs)

        self.fried_ind= MathTex("\\left(\\frac{\\dot{a}}{a}\\right)^{2}","=", "-\\frac{1}{a^{2}}","+", "\\frac{8 \\pi}{3}","2  \\left(\\frac{1}{k_{-}}-\\frac{1}{k_{+}}\\right)^{-1} G_{5}"," \\left(\\sigma_{cr}- \\sigma\\right)","+ \\mathcal{O}(\\epsilon^{2})",color = my_color, font_size = my_font_size)
        self.fried_usual= MathTex("\\left(\\frac{\\dot{a}}{a}\\right)^{2}","=", "-\\frac{1}{a^{2}}","+", "\\frac{8 \\pi}{3}","G_{4}"," \\rho_{\\Lambda}","+ \\mathcal{O}(\\epsilon^{2})",color = my_color, font_size = my_font_size)
        self.fried_matter= MathTex("\\left(\\frac{\\dot{a}}{a}\\right)^{2}","=", "-\\frac{1}{a^{2}}","+", "\\frac{8 \\pi}{3}","G_{4}"," \\left(\\Lambda_{4}","+","\\frac{1}{2 \\pi^{2}}\\left(\\tfrac{M_{+}}{k_{+}}- \\tfrac{M_{-}}{k_{-}}\\right)\\frac{1}{a^{4}}\\right)",color = my_color, font_size = my_font_size)
        self.fried_strings= MathTex("\\left(\\frac{\\dot{a}}{a}\\right)^{2}","=", "-\\frac{1}{a^{2}}","+", "\\frac{8 \\pi}{3}","G_{4}"," \left(\\Lambda_{4}","+","\\frac{3}{8 \\pi a^{3}}\\left(\\tfrac{\\alpha_{+}}{k_{+}}- \\tfrac{\\alpha_{-}}{k_{-}}\\right) \\right)",color = my_color, font_size = my_font_size)
        self.fried_gw= MathTex("\\left(\\frac{a'(\\eta)}{a(\\eta)}\\right)^{2}","=", "-\\frac{1}{a^{2}}","+", "\\frac{8 \\pi}{3}","G_{4}"," \\left(\\Lambda_{4}","+","3 \\zeta^{2}\\left(\\frac{q_{1}}{a^{2}}- \\frac{q_{3}}{H^{2}a^{4}}\\right) \\right)",color = my_color, font_size = my_font_size)
        self.fried_ind_bh_rs= MathTex("\\dot{a}^2=\\frac{1}{4 \\sigma^2 a^2}\\left[\\left(k_{-}^2-k_{+}^2\\right) a^2+\\left(f_{-}(a)-f_{+}(a)\\right)\\right]^2+\\frac{\\sigma^2}{4} a^2-\\frac{1}{2}\\left[\\left(f_{-}(a)+f_{+}(a)\\right)+\\left(k_{-}^2+k_{+}^2\\right) a^2\\right]",color = my_color, font_size = my_font_size)
        self.fried_ind_bh_dbi= MathTex("\\dot{\\mathcal{Z}}^2","=","-f(\\mathcal{Z})-k^2 \\mathcal{Z}^2+\\frac{k^2}{k^2 J_c^2+\\mathcal{Z}^6}\\left(\\mathcal{Z}^4-\\mathcal{Z}_H^4+\\frac{\\theta \\kappa_5 J_c}{\\mathcal{Z}_H^2}\\left(1-\\frac{\\mathcal{Z}_H^2}{\\mathcal{Z}^2}\\right)\\right)^2",color = my_color, font_size = my_font_size)
        self.fried_ind_bh_rs_junc= MathTex("\\dot{a}^2","=","-f(a)-k^2 a^2+\\frac{k^2}{a^6}\\left(a^4-a_H^4-\\frac{\\kappa_5^2 \\theta \\Delta \\theta}{a_H^2 k \\Delta k}\\left(1-\\frac{a_H^2}{a^2}\\right)\\right)^2",color = my_color, font_size = my_font_size)

## Actions and Hamiltonians

class EqAction(MathTex):
    """class as a collection of actions and hamiltonians.

    Parameters:
        - color: no need to explain.
        - size: font_size.
    """
    def __init__(self,my_color, my_font_size, **kwargs):
        super().__init__(**kwargs)

        self.bubble_action_5d = MathTex("\\mathcal{S}=","\\frac{1}{2 \\kappa_{5}} \\int d^{5} x \\sqrt{|g|}\\left(R^{(5)}-2 \\Lambda_{5}\\right)","-","\\sigma \\int d^{4} \\zeta \\sqrt{|\\eta|}","+","\\frac{1}{\\kappa_{5}} \\oint d^{4} x \\sqrt{|h|} K ",color = my_color, font_size = my_font_size)
        self.hamil_quantum_5d= MathTex("\\mathcal{H} \\psi_{5D}=","\\left(\\left(-\\frac{1}{24 \\pi^{2}}\\frac{1}{a^{3 / 2}} \\frac{d^{2}}{d a^{2}}\\right)+6 \\pi^{2} V(a)\\right)","a^{3 / 2} \\psi_{5D}","=0",color = my_color, font_size = my_font_size)
        self.dbi_action = MathTex("S_{D 3}","=","-T_3 \\int d^4 \\xi \\sqrt{- det P[G]}","+","T_3 \\int P\\left[C_4\\right]",color = my_color, font_size = my_font_size)
        self.hamil_from_dbi = MathTex("\mathcal{H}","=","2 \\pi^2 T_3\\left(\\sqrt{-g_{tt}\\left(\\mathcal{Z}^6+\\frac{J_C^2}{L^2}\\right)} \\sqrt{1+g_{zz} \\dot{\\mathcal{Z}}^2}-\\left(C_4\\right)_{t}-\\frac{A_t}{L}", "J_c","\\right)",color = my_color, font_size = my_font_size)

## Junctions

class EqJunc(MathTex):
    """class as a collection of junction condition equations.

    Parameters:
        - color: no need to explain.
        - size: font_size.
    """
    def __init__(self, my_color, my_font_size, **kwargs):
        super().__init__(**kwargs)

        self.junc = MathTex(r' h_{ab}^{(+)} &= h_{ab}^{(-)}\\ S_{ab} &= \kappa_{5}^{-1}\left([\Delta K_{ab}]^{+}_{-} -[\Delta K]^{+}_{-}h_{ab}\right)',color = my_color, font_size = my_font_size)
        self.junc_db = MathTex(r'S_{ab} &= \kappa_{5}^{-1}\left([K_{ab}^{(+)} - K_{ab}^{(-)}]-[K^{(+)} - K^{(-)}]h_{ab}\right)',color = my_color, font_size = my_font_size)
        self.crit_t_rs= MathTex(r' \sigma = \frac{3 \left(k + k\right)}{\kappa_{5}}',color = my_color, font_size = my_font_size)
        self.crit_t_db= MathTex(r' \sigma_{cr} = \frac{3}{\kappa_{5}}\left(k_{-}-k_{+}\right)',color = my_color, font_size = my_font_size)
        self.brane_t_db= MathTex(r'\sigma &= \frac{3}{\kappa^{2}_{5}} \left(\sqrt{k_{-}^{2} + \frac{1+ \dot{a}^{2}}{a^{2}}} -\sqrt{k_{+}^{2} + \frac{1+ \dot{a}^{2}}{a^{2}}} \right)',color = my_color, font_size = my_font_size)
        self.junc_bh_rs = MathTex("T_3=\\frac{3}{\\kappa_5^2}\\left(\\sqrt{\\frac{g_{-}(a)+\\dot{a}^2}{a^2}}-\\sqrt{\\frac{g_{+}(a)+\\dot{a}^2}{a^2}}\\right)",color = my_color, font_size = my_font_size)

## Quantum

class EqQuan(MathTex):
    """class as a collection of quantum cosmology equations.
    
    Parameters:
        - color: no need to explain.
        - size: font_size.
    """
    def __init__(self, my_color, my_font_size, **kwargs):
        super().__init__(**kwargs)

        self.wdw= MathTex("\\mathcal{H} \\psi(a)= \\frac{N}{a} \\left(-\\frac{1}{24 \\pi^{2}} \\frac{d^{2}}{da^{2}} + 6 \\pi^{2}", "\\left(a^{2} -\\frac{a^{4}}{a_{0}^{2}}\\right)","\\right)\\psi(a)= 0",color = my_color, font_size = my_font_size)
        wkbwavespsi= MathTex(r'\Psi(a) =')
        wkbwaves0= MathTex(r' \left\{',font_size=70).next_to(wkbwavespsi, RIGHT)
        wkbwaves1= MathTex(r'a \:e^{S(a_{0},0)} + b\: e^{-S(a_{0},0)},& \quad a \leq a_{0} \\c \:e^{i\:S(a,a_{0})} + d\: e^{-i\: S(a,a_{0})}, & \quad a \geq a_{0}').next_to(wkbwaves0, RIGHT)
        self.wkbwaves= VGroup(wkbwavespsi,wkbwaves0,wkbwaves1)
        hh = MathTex("P_{HH} \propto e^{+2 S_{0}}" ,color = DARK_BLUE, font_size = my_font_size)
        vv = MathTex("P_{V} \propto e^{-2 S_{0}}",color = RED, font_size = my_font_size)
        self.weights= VGroup(hh,vv).arrange(DOWN, aligned_edge = LEFT)
        self.nucprobBT= MathTex("P \propto e^{-B}", "=e^","{ \\frac{-8 \\pi^{2} a_{0}^{2}}{\\kappa_{4}}}",color = my_color, font_size = my_font_size)
        self.nucprobWKB= MathTex("P \propto e^{-2 \\int p d\\tau}","=e^","{\\frac{-8 \\pi^{2} a_{0}^{2}}{\\kappa_{4}}}",color = my_color, font_size = my_font_size)
        self.nucprobBT2= MathTex("P \propto e^{-B}", "=e^","{ \\frac{-c}{\\Lambda_{4}}}",color = my_color, font_size = my_font_size)
        self.nucprobWKB2= MathTex("P \propto e^{-2 \\int p d\\tau}","=e^","{\\frac{-c}{\\Lambda_{4}}}",color = my_color, font_size = my_font_size)
        self.nucprob = VGroup(self.nucprobBT, self.nucprobWKB).arrange(LEFT, buff =2)
        self.nucprob_2 = VGroup(self.nucprobBT2, self.nucprobWKB2).arrange(LEFT, buff =2)
        
class Scale_Discussion(MathTex):
    """class as a collection of scale separation discussion.

    Parameters:
        - color: no need to explain.
        - size: font_size.
    """
    def __init__(self, my_color, my_font_size, **kwargs):
        super().__init__(**kwargs)
        
        scales = ["L", "l_{10}", "l_{5}", "l_{4}"]
        spaces = ["M_{10}", "AdS_{5} \\times S^{5}"]
        #color_discussion = [PURPLE_E, DARK_BLUE, GREEN, RED_E]
        kappas = ["\\kappa_{10} \sim l^{8}_{10}", "\\kappa_{5} \sim \\frac{l^{8}_{10}}{L^{5}}", "\\kappa_{5} \sim \\frac{L^{3}}{N^{2}}", "\\kappa_{10} \sim N^{5/12} l_{5}"]
        hierarchy = ["L > l_{10} > l_{5}", "N^{2/3}l_{5} > N^{5/12}l_{5} > l_{5}", "L > l_{10} > l_{4} > l_{5}", "N^{1/2}l_{4} > N^{1/4}l_{4} > l_{4} > N^{-1/6} l_{4}", "10^{-5} m > 10^{-20} m > 10^{-35} m > 10^{-45} m", "3.8 \\, meV < 13.7 \\, TeV < 1.22 \\times 10^{19} \\, GeV  < 5.1 \\times 10^{31}  \\, GeV"]
        LNgame = ["\\kappa_{5} \sim \\frac{L^{3}}{N^{2}}","\\frac{\\Delta L}{L} \sim \\frac{\\Delta N}{N}"]
        tension_game = ["\\sigma_{cr} = \\frac{3 \\Delta k}{\\kappa_{5}}", "\\sigma_{cr} = -\\frac{3 \\Delta L}{\\kappa_{5} L^{2}}","\\sigma_{cr} = - \\Delta N T_{D3}"]
        g4_game = ["G_{4} \sim \\frac{k_{+} k_{-}}{k_{-} - k_{+}} G_{5}", "G_{4} \sim \\frac{N}{L} G_{5}"]
        
        
        self.L_curvature = MathTex("L^{4}" ,"=" , " 4 \\pi g_{s} \\alpha'^{2}", "N" ,color = my_color, font_size = my_font_size)
        self.scales_math= VGroup(*[MathTex(scales[i], font_size = my_font_size, color = my_color) for i in range(len(scales))])
        self.spaces = VGroup(*[MathTex(spaces[i], font_size = my_font_size/(i+1), color = my_color)for i in range(len(spaces))])
        self.kappas = VGroup(*[MathTex(kappas[i], font_size = my_font_size, color = my_color) for i in range(len(kappas))])
        self.hierarchy = VGroup(*[MathTex(hierarchy[i], font_size = my_font_size, color = my_color) for i in range(len(hierarchy))])
        self.LNgame= VGroup(*[MathTex(LNgame[i], font_size = my_font_size, color = my_color) for i in range(len(LNgame))])
        self.tension_game = VGroup(*[MathTex(tension_game[i], font_size = my_font_size, color = my_color) for i in range(len(tension_game))])
        self.g4_game = VGroup(*[MathTex(g4_game[i], font_size = my_font_size, color = my_color) for i in range(len(g4_game))])
        

class D3_corrections(MathTex):
    """class as a collection for the D3 action + corrections .

    Parameters:
        - color: no need to explain.
        - size: font_size.
    """
    def __init__(self, my_color, my_font_size, **kwargs):
        super().__init__(**kwargs)
        actionD3 = ["S[g_{\\mu \\nu}, C_{4}] = \\text{DBI}^{(0)} + \\alpha'^{2} \\text{DBI}^{(2)} + \\text{WZ}^{(0)} + \\alpha'^{2} \\text{WZ}^{(2)}",
                    "\\sigma \sim T_{D3} \\left(1 - \\frac{\\alpha'^{2}}{L^{4}}\\right)",
                    "\\sigma \sim \\sigma_{cr} \\left(1 - \\frac{1}{g_{s} N}\\right)"]
        new_lambda = ["N = \\sqrt{\\frac{3 \\pi}{G_{4}^{2} g_{s} \\rho_{\\Lambda}}}", "N \sim 10^{60}"]
        
        self.actionD3 = VGroup(*[MathTex(actionD3[i], font_size = my_font_size, color = my_color) for i in range(len(actionD3))])
        self.new_lambda = VGroup(*[MathTex(new_lambda[i], font_size = my_font_size, color = my_color) for i in range(len(new_lambda))])

class EM_action(MathTex):
    """class as a collection of equation to describe EM in bulk.

    Parameters:
        - color: no need to explain.
        - size: font_size.
    """
    def __init__(self, my_color, my_font_size, **kwargs):
        super().__init__(**kwargs)
        self.actionEM = MathTex("S_{5}[H, \\mathcal{F}] \sim \int d^{5}x \\sqrt{g_{5}} \\: \\left(R - H^{2}\\right) - T_{D3} \int d^{5}x \\: \\delta \\left(r - a(\\eta)\\right) \\:\\sqrt{g_{4} + \\mathcal{F}}", font_size = my_font_size, color = my_color)
        self.EOM = MathTex("\\partial_r H^{r\\mu \\nu} = \\frac{2 \\kappa_{5} \\:kr}{\\alpha'\\: \\pi^{2} } \\:{\\mathcal{F}}^{\\mu \\nu} \\:\\delta \\left(r-a(\\eta)\\right)")
        
        


