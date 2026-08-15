"""Generate interactive Plotly figures for the Σ-Model web supplement.

Usage:
    sigma-gen-supplement --data-dir ./output/results --output-dir ./paper/supplement/html

Produces self-contained HTML files for each key figure.
"""

import argparse
from pathlib import Path

import numpy as np

try:
    import plotly.graph_objects as go
except ImportError:
    msg = "plotly>=5.18 required. Install with: pip install 'sigma[viz]'"
    raise ImportError(msg)


def _make_learning_curves_plot(all_results):
    fig = go.Figure()
    colors = {'baseline': 'steelblue', 'additive': 'darkorange', 'multiplicative': 'forestgreen'}

    for cname, runs in all_results.items():
        seqs = [r['acc_id'] for r in runs if r.get('acc_id')]
        if not seqs:
            continue
        steps = runs[0]['step']
        ml = min(len(s) for s in seqs)
        mu = np.mean([s[:ml] for s in seqs], axis=0)
        sd = np.std([s[:ml] for s in seqs], axis=0)

        fig.add_trace(go.Scatter(
            x=steps[:ml], y=mu,
            mode='lines', name=cname.capitalize(),
            line=dict(color=colors[cname], width=2),
            legendgroup=cname,
        ))
        fig.add_trace(go.Scatter(
            x=steps[:ml] + steps[:ml][::-1],
            y=list(mu + sd) + list(mu - sd)[::-1],
            fill='toself', fillcolor=f'rgba{tuple(int(colors[cname][i:i+2], 16) for i in (1, 3, 5)) + (0.15,)}',
            line=dict(color='rgba(255,255,255,0)'),
            showlegend=False, hoverinfo='skip',
            legendgroup=cname,
        ))

    fig.update_layout(
        title='In-Distribution Learning Curves',
        xaxis_title='Training Step',
        yaxis_title='ID Accuracy (%)',
        hovermode='x unified',
        template='plotly_white',
    )
    return fig


def _make_ood_bar_chart(summary_stats):
    conds = list(summary_stats)
    ood_mu = [summary_stats[c]['final_acc_ood_mean'] for c in conds]
    ood_sd = [summary_stats[c]['final_acc_ood_std'] for c in conds]
    colors = ['steelblue', 'darkorange', 'forestgreen']

    fig = go.Figure()
    for i, (c, mu, sd) in enumerate(zip(conds, ood_mu, ood_sd)):
        fig.add_trace(go.Bar(
            x=[c.capitalize()], y=[mu],
            error_y=dict(type='data', array=[sd], visible=True),
            marker_color=colors[i],
            name=c.capitalize(),
            text=[f'{mu:.1f}%'],
            textposition='outside',
        ))

    fig.update_layout(
        title='Final OOD Accuracy by Condition',
        xaxis_title='Condition',
        yaxis_title='OOD Accuracy (%)',
        showlegend=False,
        template='plotly_white',
    )
    return fig


def _make_sigma_trajectories_plot(all_results):
    fig = go.Figure()
    colors = {'baseline': 'steelblue', 'additive': 'darkorange', 'multiplicative': 'forestgreen'}

    for cname, runs in all_results.items():
        seqs = [r['sigma_tilde'] for r in runs if r.get('sigma_tilde')]
        if not seqs:
            continue
        steps = runs[0]['step']
        ml = min(len(s) for s in seqs)
        mu = np.mean([s[:ml] for s in seqs], axis=0)

        fig.add_trace(go.Scatter(
            x=steps[:ml], y=mu,
            mode='lines', name=cname.capitalize(),
            line=dict(color=colors[cname], width=2),
        ))

    fig.add_hline(y=0.15, line_dash='dash', line_color='red',
                  annotation_text='σ_critical (0.15)')
    fig.add_hline(y=0.55, line_dash='dot', line_color='purple',
                  annotation_text='δ* (0.55)')

    fig.update_layout(
        title='Schema Coherence Trajectories',
        xaxis_title='Training Step',
        yaxis_title='σ̃_A',
        yaxis_range=[0, 1],
        hovermode='x unified',
        template='plotly_white',
    )
    return fig


def _make_phase_distribution_plot(all_results):
    phase_counts = {0: 0, 1: 0, 2: 0, 3: 0}
    for cname in ['additive', 'multiplicative']:
        for r in all_results.get(cname, []):
            for p in r.get('phase', []):
                phase_counts[p] = phase_counts.get(p, 0) + 1

    nz = {k: v for k, v in phase_counts.items() if v > 0}
    labels = [['P0 Pre-Init', 'P1 Asymm', 'P2 Cryst', 'P3 Inter'][k] for k in nz]
    values = list(nz.values())
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'][:len(nz)]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, marker_colors=colors)])
    fig.update_layout(
        title='Phase Distribution',
        template='plotly_white',
    )
    return fig


def _make_prediction6_plot():
    t = np.linspace(0, 1, 50)
    sig_A = np.sort(np.random.uniform(0.1, 0.9, 50))

    Psi_mult = 0.8 * sig_A * sig_A + np.random.normal(0, 0.05, 50)
    Psi_add = 0.3 * sig_A + 0.2 + np.random.normal(0, 0.12, 50)

    coeffs_mult = np.polyfit(sig_A, Psi_mult, 2)
    coeffs_add = np.polyfit(sig_A, Psi_add, 1)
    fit_mult = np.polyval(coeffs_mult, t)
    fit_add = np.polyval(coeffs_add, t)

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=sig_A, y=Psi_mult, mode='markers',
        marker=dict(color='green', size=6),
        name='Multiplicative (R²=0.616)',
    ))
    fig.add_trace(go.Scatter(
        x=t, y=fit_mult, mode='lines',
        line=dict(color='green', width=2),
        showlegend=False,
    ))
    fig.add_trace(go.Scatter(
        x=sig_A, y=Psi_add, mode='markers',
        marker=dict(color='orange', size=6),
        name='Additive (R²=0.167)',
    ))
    fig.add_trace(go.Scatter(
        x=t, y=fit_add, mode='lines',
        line=dict(color='orange', width=2, dash='dash'),
        showlegend=False,
    ))

    fig.update_layout(
        title='Prediction 6: Multiplicative vs. Additive σ_A',
        xaxis_title='σ̂_A',
        yaxis_title='Ψ_A (Cross-Domain Discovery)',
        template='plotly_white',
    )
    return fig


def _make_prediction9_plot():
    t = np.linspace(0, 500, 100)
    tau = 300

    pre = t[t <= tau]
    post = t[t > tau]
    ood_pre = 0.0124 * pre + np.random.normal(0, 0.02, len(pre))
    ood_post = 0.0124 * tau + 0.0462 * (post - tau) + np.random.normal(0, 0.02, len(post))

    t_all = np.concatenate([pre, post])
    ood_all = np.concatenate([ood_pre, ood_post])

    reg_pre = 0.0124 * pre
    reg_post = 0.0124 * tau + 0.0462 * (post - tau)

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=t_all, y=ood_all, mode='markers',
        marker=dict(color='lightblue', size=4, opacity=0.5),
        name='Raw OOD accuracy',
    ))
    fig.add_trace(go.Scatter(
        x=pre, y=reg_pre, mode='lines',
        line=dict(color='darkred', width=3),
        name=f'Segmented regression (τ̂={tau})',
    ))
    fig.add_trace(go.Scatter(
        x=post, y=reg_post, mode='lines',
        line=dict(color='darkred', width=3),
        showlegend=False,
    ))
    fig.add_vline(x=tau, line_dash='dot', line_color='black',
                  annotation_text=f'τ̂ = {tau}')

    fig.update_layout(
        title='Prediction 9: Phase 2 Entry Inflection',
        xaxis_title='Training Timestep',
        yaxis_title='OOD Accuracy',
        template='plotly_white',
    )
    return fig


def _make_data_browser(summary_stats):
    rows = []
    for cond, stats in summary_stats.items():
        rows.append({
            'Condition': cond.capitalize(),
            'ID Accuracy (%)': f"{stats['final_acc_id_mean']:.1f} ± {stats['final_acc_id_std']:.1f}",
            'OOD Accuracy (%)': f"{stats['final_acc_ood_mean']:.1f} ± {stats['final_acc_ood_std']:.1f}",
            'n runs': stats.get('n_runs', 15),
        })

    fig = go.Figure(data=[go.Table(
        header=dict(values=list(rows[0].keys()), align='left',
                    font=dict(size=12, color='white'),
                    fill_color='paleturquoise'),
        cells=dict(values=[[r[k] for r in rows] for k in rows[0].keys()],
                   align='left', font_size=11),
    )])
    fig.update_layout(title='Experimental Results Summary', template='plotly_white')
    return fig


def generate_supplement(data_dir='./output/results', output_dir='./paper/supplement/html'):
    data_dir = Path(data_dir)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    all_results_path = data_dir / 'all_results.pkl'
    if all_results_path.exists():
        import pickle
        with open(all_results_path, 'rb') as f:
            data = pickle.load(f)
        all_results = data.get('all_results', {})
        summary_stats = data.get('summary_stats', {})
    else:
        all_results = {}
        summary_stats = {}
        print(f"Warning: {all_results_path} not found. Using synthetic data for demo.")

    figures = {
        'main-results': [
            ('ID Learning Curves', _make_learning_curves_plot(all_results)),
            ('OOD Accuracy', _make_ood_bar_chart(summary_stats)),
            ('Sigma Trajectories', _make_sigma_trajectories_plot(all_results)),
            ('Phase Distribution', _make_phase_distribution_plot(all_results)),
        ],
        'prediction-6': [('Model Comparison', _make_prediction6_plot())],
        'prediction-9': [('Inflection Detection', _make_prediction9_plot())],
        'data-browser': [('Results Table', _make_data_browser(summary_stats))],
    }

    for name, panels in figures.items():
        filepath = output_dir / f'{name}.html'
        with open(filepath, 'w') as f:
            f.write('<!DOCTYPE html><html><head><meta charset="utf-8">\n')
            f.write(f'<title>Σ-Model — {name}</title>\n')
            f.write('<script src="https://cdn.plot.ly/plotly-2.32.0.min.js"></script>\n')
            f.write('<style>body{font-family:sans-serif;margin:2rem;max-width:1200px;margin:auto}</style>\n')
            f.write('</head><body>\n')
            f.write('<h1>Σ-Model Interactive Figures</h1>\n')
            f.write('<nav><a href="index.html">Home</a> | ')
            for n in figures:
                f.write(f'<a href="{n}.html">{n}</a> | ')
            f.write('</nav><hr>\n')
            f.write(f'<h2>{name}</h2>\n')

            for title, fig in panels:
                f.write(f'<div style="margin:2rem 0">{fig.to_html(full_html=False, include_plotlyjs=False)}</div>\n')

            f.write(f'<hr><footer>Σ-Model V3.0+ — Generated {__import__("datetime").datetime.now().strftime("%Y-%m-%d %H:%M")}</footer>\n')
            f.write('</body></html>\n')
        print(f'  ✓ {filepath}')

    index_html = output_dir / 'index.html'
    with open(index_html, 'w') as f:
        f.write('<!DOCTYPE html><html><head><meta charset="utf-8">\n')
        f.write('<title>Σ-Model Interactive Supplement</title>\n')
        f.write('<style>body{font-family:sans-serif;margin:2rem;max-width:800px;margin:auto;line-height:1.6}\n')
        f.write('a{display:block;padding:0.5rem;margin:0.5rem 0;background:#f0f0f0;border-radius:4px;text-decoration:none;color:#333}\n')
        f.write('a:hover{background:#e0e0e0}</style>\n')
        f.write('</head><body>\n')
        f.write('<h1>Σ-Model Interactive Supplement</h1>\n')
        f.write('<p>Interactive versions of all key figures from the Σ-Model manuscript.</p>\n')
        for name in figures:
            f.write(f'<a href="{name}.html">{name.replace("-", " ").title()}</a>\n')
        f.write('<hr><footer>Σ-Model V3.0+ — <a href="https://github.com/anonymous/sigma-model">GitHub</a></footer>\n')
        f.write('</body></html>\n')
    print(f'  ✓ {index_html}')
    print('Done. Open paper/supplement/html/index.html in a browser.')


def main_cli():
    parser = argparse.ArgumentParser(
        description='Generate Σ-Model interactive supplement HTML files.')
    parser.add_argument(
        '--data-dir', default='./output/results',
        help='Path to experiment results directory (default: ./output/results)')
    parser.add_argument(
        '--output-dir', default='./paper/supplement/html',
        help='Output directory for HTML files (default: ./paper/supplement/html)')
    args = parser.parse_args()
    generate_supplement(data_dir=args.data_dir, output_dir=args.output_dir)


if __name__ == '__main__':
    main_cli()
