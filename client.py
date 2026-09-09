import math

class STDPSynapse:
    """Spike-Timing-Dependent Plasticity (STDP) synaptic weight adapter."""
    def __init__(self, initial_weight: float = 0.5, w_min: float = 0.0, w_max: float = 1.0,
                 a_plus: float = 0.01, a_minus: float = 0.0105,
                 tau_plus: float = 20.0, tau_minus: float = 20.0):
        self.w = initial_weight
        self.w_min = w_min
        self.w_max = w_max
        self.a_plus = a_plus
        self.a_minus = a_minus
        self.tau_plus = tau_plus
        self.tau_minus = tau_minus

    def update_weight(self, t_pre: float, t_post: float) -> dict:
        delta_t = t_post - t_pre
        if delta_t > 0:
            # Pre before Post: LTP (Long-Term Potentiation)
            dw = self.a_plus * math.exp(-delta_t / self.tau_plus)
            event = "LTP"
        elif delta_t < 0:
            # Post before Pre: LTD (Long-Term Depression)
            dw = -self.a_minus * math.exp(delta_t / self.tau_minus)
            event = "LTD"
        else:
            dw = 0.0
            event = "NONE"

        old_w = self.w
        self.w = max(self.w_min, min(self.w_max, self.w + dw))

        return {
            "t_pre": t_pre,
            "t_post": t_post,
            "delta_t": round(delta_t, 2),
            "event": event,
            "delta_w": round(dw, 6),
            "old_weight": round(old_w, 6),
            "new_weight": round(self.w, 6)
        }
