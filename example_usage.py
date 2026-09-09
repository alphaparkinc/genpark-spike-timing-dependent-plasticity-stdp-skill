from client import STDPSynapse

def main():
    print("=== STDP Synaptic Learning Rule Simulator ===")
    synapse = STDPSynapse(initial_weight=0.5)

    # Pre-synaptic spike at t=10ms, Post-synaptic spike at t=15ms (delta_t = +5ms -> LTP)
    res_ltp = synapse.update_weight(t_pre=10.0, t_post=15.0)
    print("LTP Step:", res_ltp)
    assert res_ltp["new_weight"] > res_ltp["old_weight"]

    # Pre-synaptic spike at t=30ms, Post-synaptic spike at t=25ms (delta_t = -5ms -> LTD)
    res_ltd = synapse.update_weight(t_pre=30.0, t_post=25.0)
    print("LTD Step:", res_ltd)
    assert res_ltd["new_weight"] < res_ltd["old_weight"]

    print("STDP Synaptic Learning Rule verified successfully!")

if __name__ == "__main__":
    main()
