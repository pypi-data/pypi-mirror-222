import numpy as np
import scipy
from mpoints import hybrid_hawkes_exp


def produce_samples(
):
    number_of_event_types: int = 5
    de = number_of_event_types
    number_of_states: int = 9
    dx = number_of_states
    events_labels = [chr(65 + n) for n in range(number_of_event_types)]
    states_labels = [chr(48 + n) for n in range(number_of_states)]
    _phis = [np.eye(dx) + scipy.sparse.random(dx, dx,
                                              density=.50).A for _ in range(de)]
    _phis = [_phi / 10*np.sum(_phi, axis=1, keepdims=True)
             for _phi in _phis]
    _phis = [np.expand_dims(_phi, axis=1) for _phi in _phis]
    phis = np.concatenate(_phis, axis=1)
    nus = np.random.uniform(low=0., high=1., size=(de,))
    alphas = .5 * scipy.sparse.random(de, dx*de, density=.50).A.reshape(de, dx, de)
    betas = np.ones((de, dx, de), dtype=float)
    hhe = hybrid_hawkes_exp.HybridHawkesExp(
        number_of_event_types,
        number_of_states,
        events_labels,
        states_labels,
    )
    hhe.set_transition_probabilities(phis)
    hhe.set_hawkes_parameters(nus, alphas, betas)
    time_start = 0.
    time_end = 10000.
    times, events, states = hhe.simulate(
        time_start, time_end, max_number_of_events=1000000)
    return hhe, times, events, states
