/**
 * Sigma-Model Research Portal Interactive App
 * Powers the dynamic phase portrait, change-point visualizer, and interactivity.
 */

document.addEventListener("DOMContentLoaded", () => {
  initTheme();
  initPhasePortrait();
  initChangePointPlot();
  initCopyButtons();
});

/* Theme Handling */
function initTheme() {
  const toggleBtn = document.getElementById("themeToggle");
  const storedTheme = localStorage.getItem("sigma_theme");
  const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
  
  if (storedTheme) {
    document.documentElement.setAttribute("data-theme", storedTheme);
  } else if (prefersDark) {
    document.documentElement.setAttribute("data-theme", "dark");
  }

  if (toggleBtn) {
    toggleBtn.addEventListener("click", () => {
      const current = document.documentElement.getAttribute("data-theme");
      const next = current === "dark" ? "light" : "dark";
      document.documentElement.setAttribute("data-theme", next);
      localStorage.setItem("sigma_theme", next);
      // Trigger canvas redrawing
      if (window.redrawPhasePortrait) window.redrawPhasePortrait();
      if (window.redrawChangePoint) window.redrawChangePoint();
    });
  }
}

/* Two-Subspace Phase Portrait Dynamical System Simulator */
function initPhasePortrait() {
  const canvas = document.getElementById("phaseCanvas");
  if (!canvas) return;
  const ctx = canvas.getContext("2d");

  // Model parameters (locked Level 1 normal form)
  const a_S = 1.0;
  const theta_S = 1.0;
  const b_S = 1.0;
  const a_C = 1.0;
  const b_C = 0.025; // Critical threshold lambda_crit = b_C / a_C = 0.025
  const kappa = 1.0;

  // DOM elements
  const lambdaSlider = document.getElementById("lambdaSlider");
  const lambdaValDisplay = document.getElementById("lambdaVal");
  const r0ValDisplay = document.getElementById("r0Val");
  const regimeStatusDisplay = document.getElementById("regimeStatus");
  const fixedPointsDisplay = document.getElementById("fixedPointsInfo");

  let currentLambda = parseFloat(lambdaSlider ? lambdaSlider.value : 0.015);
  let animationFrameId = null;

  // Trajectory particles for dynamic streamline flow
  const particles = [];
  const numParticles = 40;
  
  function resetParticles() {
    particles.length = 0;
    for (let i = 0; i < numParticles; i++) {
      particles.push({
        u: Math.random() * 1.35 + 0.05,
        v: Math.random() * 0.95 + 0.02,
        life: Math.random() * 80 + 20,
        maxLife: 100
      });
    }
  }
  resetParticles();

  function resizeCanvas() {
    const rect = canvas.getBoundingClientRect();
    const dpr = window.devicePixelRatio || 1;
    canvas.width = rect.width * dpr;
    canvas.height = rect.height * dpr;
    ctx.scale(dpr, dpr);
  }
  window.addEventListener("resize", () => {
    resizeCanvas();
  });
  resizeCanvas();

  function getDerivatives(u, v, lam) {
    const du = u * (theta_S - a_S * u - b_S * v * v);
    const dv = v * (lam * a_C - b_C - kappa * v * v);
    return { du, dv };
  }

  function render() {
    const rect = canvas.getBoundingClientRect();
    const w = rect.width;
    const h = rect.height;

    const isDark = document.documentElement.getAttribute("data-theme") === "dark";
    const bgCol = isDark ? "#0f172a" : "#f8fafc";
    const axisCol = isDark ? "#334155" : "#cbd5e1";
    const textCol = isDark ? "#94a3b8" : "#64748b";
    const arrowCol = isDark ? "rgba(148, 163, 184, 0.22)" : "rgba(100, 116, 139, 0.25)";

    ctx.clearRect(0, 0, w, h);

    // Padding & scales: u in [0, 1.5], v in [0, 1.0]
    const padL = 45;
    const padR = 25;
    const padT = 25;
    const padB = 40;
    const plotW = w - padL - padR;
    const plotH = h - padT - padB;

    function toX(u) { return padL + (u / 1.5) * plotW; }
    function toY(v) { return padT + (1.0 - (v / 1.0)) * plotH; }
    function fromX(x) { return ((x - padL) / plotW) * 1.5; }
    function fromY(y) { return (1.0 - (y - padT) / plotH) * 1.0; }

    // Grid lines & axes
    ctx.strokeStyle = axisCol;
    ctx.lineWidth = 1;
    ctx.beginPath();
    // X-axis (v = 0)
    ctx.moveTo(padL, toY(0));
    ctx.lineTo(padL + plotW, toY(0));
    // Y-axis (u = 0)
    ctx.moveTo(toX(0), padT);
    ctx.lineTo(toX(0), padT + plotH);
    ctx.stroke();

    // Axis Labels
    ctx.fillStyle = textCol;
    ctx.font = "12px sans-serif";
    ctx.textAlign = "center";
    ctx.fillText("Shortcut Coordinate u(t)", padL + plotW / 2, h - 10);
    ctx.save();
    ctx.translate(15, padT + plotH / 2);
    ctx.rotate(-Math.PI / 2);
    ctx.fillText("Schema Coordinate v(t)", 0, 0);
    ctx.restore();

    // Tick labels
    ctx.fillText("0", toX(0), toY(0) + 18);
    ctx.fillText("0.5", toX(0.5), toY(0) + 18);
    ctx.fillText("1.0", toX(1.0), toY(0) + 18);
    ctx.fillText("1.5", toX(1.5), toY(0) + 18);

    ctx.textAlign = "right";
    ctx.fillText("0.5", toX(0) - 8, toY(0.5) + 4);
    ctx.fillText("1.0", toX(0) - 8, toY(1.0) + 4);

    // Vector Field Grid
    const nx = 15;
    const ny = 10;
    for (let ix = 0; ix <= nx; ix++) {
      for (let iy = 0; iy <= ny; iy++) {
        const u = (ix / nx) * 1.45;
        const v = (iy / ny) * 0.95;
        const { du, dv } = getDerivatives(u, v, currentLambda);
        const len = Math.hypot(du, dv) || 1e-6;
        const scale = 14;
        const dx = (du / len) * scale;
        const dy = -(dv / len) * scale;

        const x0 = toX(u);
        const y0 = toY(v);

        ctx.strokeStyle = arrowCol;
        ctx.fillStyle = arrowCol;
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(x0, y0);
        ctx.lineTo(x0 + dx, y0 + dy);
        ctx.stroke();

        // Small arrow head
        const angle = Math.atan2(dy, dx);
        ctx.beginPath();
        ctx.moveTo(x0 + dx, y0 + dy);
        ctx.lineTo(x0 + dx - 4 * Math.cos(angle - Math.PI / 6), y0 + dy - 4 * Math.sin(angle - Math.PI / 6));
        ctx.lineTo(x0 + dx - 4 * Math.cos(angle + Math.PI / 6), y0 + dy - 4 * Math.sin(angle + Math.PI / 6));
        ctx.fill();
      }
    }

    // Dynamic Streamlines / Particles
    const particleCol = isDark ? "rgba(59, 130, 246, 0.75)" : "rgba(37, 99, 235, 0.75)";
    ctx.fillStyle = particleCol;
    ctx.strokeStyle = isDark ? "rgba(59, 130, 246, 0.25)" : "rgba(37, 99, 235, 0.25)";
    ctx.lineWidth = 1.5;

    const dt = 0.025;
    for (let p of particles) {
      const { du, dv } = getDerivatives(p.u, p.v, currentLambda);
      const nextU = Math.max(0, p.u + du * dt);
      const nextV = Math.max(0, p.v + dv * dt);

      ctx.beginPath();
      ctx.arc(toX(p.u), toY(p.v), 2.2, 0, Math.PI * 2);
      ctx.fill();

      p.u = nextU;
      p.v = nextV;
      p.life++;

      if (p.life > p.maxLife || p.u > 1.5 || p.v > 1.0) {
        p.u = Math.random() * 1.35 + 0.05;
        p.v = Math.random() * 0.95 + 0.02;
        p.life = 0;
      }
    }

    // Fixed Points Calculation
    // E_0 = (0, 0)
    // E_S = (theta_S / a_S, 0) = (1, 0)
    const lam_crit = b_C / a_C; // 0.025
    const isSupercritical = currentLambda > lam_crit;

    let v_star = 0;
    let u_star = theta_S / a_S;
    if (isSupercritical) {
      v_star = Math.sqrt((currentLambda * a_C - b_C) / kappa);
      u_star = Math.max(0, (theta_S - b_S * v_star * v_star) / a_S);
    }

    // Draw Fixed Point E_S (1, 0)
    const esX = toX(1.0);
    const esY = toY(0.0);
    ctx.lineWidth = 2.5;

    if (isSupercritical) {
      // Unstable saddle
      ctx.fillStyle = "#dc2626";
      ctx.strokeStyle = "#ffffff";
      ctx.beginPath();
      ctx.arc(esX, esY, 6, 0, Math.PI * 2);
      ctx.fill();
      ctx.stroke();

      ctx.fillStyle = textCol;
      ctx.textAlign = "center";
      ctx.fillText("E_S (Saddle)", esX, esY - 12);
    } else {
      // Stable sink
      ctx.fillStyle = "#16a34a";
      ctx.strokeStyle = "#ffffff";
      ctx.beginPath();
      ctx.arc(esX, esY, 7, 0, Math.PI * 2);
      ctx.fill();
      ctx.stroke();

      ctx.fillStyle = textCol;
      ctx.textAlign = "center";
      ctx.fillText("E_S (Stable Sink)", esX, esY - 14);
    }

    // Draw Fixed Point E_C if supercritical
    if (isSupercritical) {
      const ecX = toX(u_star);
      const ecY = toY(v_star);

      // Stable attractor E_C
      ctx.fillStyle = "#16a34a";
      ctx.strokeStyle = "#ffffff";
      ctx.beginPath();
      ctx.arc(ecX, ecY, 8, 0, Math.PI * 2);
      ctx.fill();
      ctx.stroke();

      // Pulsing aura around E_C
      ctx.strokeStyle = "rgba(22, 163, 74, 0.4)";
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.arc(ecX, ecY, 14, 0, Math.PI * 2);
      ctx.stroke();

      ctx.fillStyle = textCol;
      ctx.textAlign = "left";
      ctx.fillText(`E_C (Coherent Attractor)`, ecX + 12, ecY + 4);
      ctx.fillText(`u*=${u_star.toFixed(3)}, v*=${v_star.toFixed(3)}`, ecX + 12, ecY + 18);
    }

    animationFrameId = requestAnimationFrame(render);
  }

  function updateDashboard() {
    const lam_crit = b_C / a_C;
    const r0 = currentLambda / lam_crit;
    const isSuper = currentLambda > lam_crit;

    if (lambdaValDisplay) lambdaValDisplay.textContent = currentLambda.toFixed(4);
    if (r0ValDisplay) r0ValDisplay.textContent = r0.toFixed(2);

    if (regimeStatusDisplay) {
      if (isSuper) {
        regimeStatusDisplay.className = "regime-indicator regime-supercritical";
        regimeStatusDisplay.innerHTML = `
          <strong>Supercritical Regime (R₀ = ${r0.toFixed(2)} &gt; 1.0)</strong><br>
          Transcritical bifurcation occurred at &lambda;<sub>crit</sub> = 0.025. 
          Shortcut state E<sub>S</sub> destabilized into an unstable saddle. 
          Coherent schema attractor E<sub>C</sub> is <strong>globally asymptotically stable</strong>.
        `;
      } else {
        regimeStatusDisplay.className = "regime-indicator regime-subcritical";
        regimeStatusDisplay.innerHTML = `
          <strong>Subcritical Regime (R₀ = ${r0.toFixed(2)} &lt; 1.0)</strong><br>
          Standard ERM shortcut basin. Transverse schema curvature b<sub>C</sub> dominates. 
          Coherent coordinate v(t) &to; 0 suppressed. Shortcut sink E<sub>S</sub> is the <strong>unique stable sink</strong>.
        `;
      }
    }

    if (fixedPointsDisplay) {
      if (isSuper) {
        const v_star = Math.sqrt((currentLambda * a_C - b_C) / kappa);
        const u_star = Math.max(0, (theta_S - b_S * v_star * v_star) / a_S);
        fixedPointsDisplay.innerHTML = `
          &bull; <strong>E<sub>S</sub> (1.000, 0.000):</strong> Unstable Saddle (&mu;<sub>&perp;</sub> = +${(currentLambda*a_C - b_C).toFixed(3)})<br>
          &bull; <strong>E<sub>C</sub> (${u_star.toFixed(3)}, ${v_star.toFixed(3)}):</strong> Stable Node Attractor
        `;
      } else {
        fixedPointsDisplay.innerHTML = `
          &bull; <strong>E<sub>S</sub> (1.000, 0.000):</strong> Stable Sink (&mu;<sub>&perp;</sub> = ${(currentLambda*a_C - b_C).toFixed(3)} &lt; 0)<br>
          &bull; <strong>E<sub>C</sub>:</strong> Unphysical (v*<sup>2</sup> &lt; 0, suppressed)
        `;
      }
    }
  }

  if (lambdaSlider) {
    lambdaSlider.addEventListener("input", (e) => {
      currentLambda = parseFloat(e.target.value);
      updateDashboard();
    });
  }

  window.redrawPhasePortrait = () => {
    resizeCanvas();
  };

  updateDashboard();
  render();
}

/* Change-Point Empirical Logistic Curve Visualizer */
function initChangePointPlot() {
  const canvas = document.getElementById("changePointCanvas");
  if (!canvas) return;
  const ctx = canvas.getContext("2d");

  // Empirical dense grid data on hbar (11 levels x 30 seeds = 330 runs)
  const denseData = [
    { lambda: 0.000, escaped: 2, total: 30, pct: 0.0667 },
    { lambda: 0.010, escaped: 4, total: 30, pct: 0.1333 },
    { lambda: 0.015, escaped: 8, total: 30, pct: 0.2667 },
    { lambda: 0.018, escaped: 9, total: 30, pct: 0.3000 },
    { lambda: 0.020, escaped: 10, total: 30, pct: 0.3333 },
    { lambda: 0.022, escaped: 13, total: 30, pct: 0.4333 },
    { lambda: 0.025, escaped: 18, total: 30, pct: 0.6000 },
    { lambda: 0.028, escaped: 23, total: 30, pct: 0.7667 },
    { lambda: 0.030, escaped: 25, total: 30, pct: 0.8333 },
    { lambda: 0.050, escaped: 30, total: 30, pct: 1.0000 },
    { lambda: 0.060, escaped: 30, total: 30, pct: 1.0000 }
  ];

  // Fitted Logistic model: k = 79.48, lambda_crit = 0.0238
  const k_fit = 79.48;
  const lam_crit_fit = 0.0238;
  function p_fit(lam) {
    return 1.0 / (1.0 + Math.exp(-k_fit * (lam - lam_crit_fit)));
  }

  function resize() {
    const rect = canvas.getBoundingClientRect();
    const dpr = window.devicePixelRatio || 1;
    canvas.width = rect.width * dpr;
    canvas.height = rect.height * dpr;
    ctx.scale(dpr, dpr);
    draw();
  }
  window.addEventListener("resize", resize);

  function draw() {
    const rect = canvas.getBoundingClientRect();
    const w = rect.width;
    const h = rect.height;

    const isDark = document.documentElement.getAttribute("data-theme") === "dark";
    const axisCol = isDark ? "#334155" : "#cbd5e1";
    const textCol = isDark ? "#94a3b8" : "#64748b";
    const gridCol = isDark ? "rgba(51, 65, 85, 0.4)" : "rgba(226, 232, 240, 0.6)";

    ctx.clearRect(0, 0, w, h);

    const padL = 50;
    const padR = 30;
    const padT = 30;
    const padB = 45;
    const plotW = w - padL - padR;
    const plotH = h - padT - padB;

    const maxLam = 0.060;
    function toX(lam) { return padL + (lam / maxLam) * plotW; }
    function toY(p) { return padT + (1.0 - p) * plotH; }

    // Grid lines & Y ticks
    ctx.strokeStyle = gridCol;
    ctx.lineWidth = 1;
    ctx.fillStyle = textCol;
    ctx.font = "11px sans-serif";
    ctx.textAlign = "right";

    const yTicks = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0];
    for (let yt of yTicks) {
      const y = toY(yt);
      ctx.beginPath();
      ctx.moveTo(padL, y);
      ctx.lineTo(padL + plotW, y);
      ctx.stroke();
      ctx.fillText((yt * 100).toFixed(0) + "%", padL - 8, y + 4);
    }

    // X ticks
    ctx.textAlign = "center";
    const xTicks = [0.000, 0.010, 0.020, 0.030, 0.040, 0.050, 0.060];
    for (let xt of xTicks) {
      const x = toX(xt);
      ctx.beginPath();
      ctx.moveTo(x, padT);
      ctx.lineTo(x, padT + plotH);
      ctx.stroke();
      ctx.fillText(xt.toFixed(2), x, toY(0.0) + 18);
    }

    // Critical boundary dashed line at 0.025
    const critX = toX(0.025);
    ctx.strokeStyle = "#dc2626";
    ctx.lineWidth = 1.5;
    ctx.setLineDash([4, 4]);
    ctx.beginPath();
    ctx.moveTo(critX, padT);
    ctx.lineTo(critX, padT + plotH);
    ctx.stroke();
    ctx.setLineDash([]);

    ctx.fillStyle = "#dc2626";
    ctx.textAlign = "center";
    ctx.font = "bold 11px sans-serif";
    ctx.fillText("λ_crit = 0.025", critX, padT - 8);

    // Plot fitted logistic curve
    ctx.strokeStyle = isDark ? "#60a5fa" : "#2563eb";
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    const steps = 150;
    for (let i = 0; i <= steps; i++) {
      const lam = (i / steps) * maxLam;
      const p = p_fit(lam);
      const x = toX(lam);
      const y = toY(p);
      if (i === 0) ctx.moveTo(x, y);
      else ctx.lineTo(x, y);
    }
    ctx.stroke();

    // Plot empirical data points (scatter points)
    for (let pt of denseData) {
      const x = toX(pt.lambda);
      const y = toY(pt.pct);

      ctx.fillStyle = isDark ? "#38bdf8" : "#0284c7";
      ctx.strokeStyle = "#ffffff";
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.arc(x, y, 6, 0, Math.PI * 2);
      ctx.fill();
      ctx.stroke();
    }

    // Axis labels
    ctx.fillStyle = textCol;
    ctx.font = "12px sans-serif";
    ctx.textAlign = "center";
    ctx.fillText("Compositional Pressure λ", padL + plotW / 2, h - 8);

    ctx.save();
    ctx.translate(15, padT + plotH / 2);
    ctx.rotate(-Math.PI / 2);
    ctx.fillText("Escape Probability P(Acc ≥ 80%)", 0, 0);
    ctx.restore();

    // Legend
    const legX = padL + 15;
    const legY = padT + 20;
    ctx.fillStyle = isDark ? "#1e293b" : "#ffffff";
    ctx.strokeStyle = axisCol;
    ctx.lineWidth = 1;
    ctx.fillRect(legX, legY, 195, 55);
    ctx.strokeRect(legX, legY, 195, 55);

    // Curve legend
    ctx.strokeStyle = isDark ? "#60a5fa" : "#2563eb";
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    ctx.moveTo(legX + 10, legY + 18);
    ctx.lineTo(legX + 30, legY + 18);
    ctx.stroke();

    ctx.fillStyle = isDark ? "#f8fafc" : "#0f172a";
    ctx.textAlign = "left";
    ctx.font = "11px sans-serif";
    ctx.fillText("Logistic Fit (k = 79.5)", legX + 38, legY + 22);

    // Point legend
    ctx.fillStyle = isDark ? "#38bdf8" : "#0284c7";
    ctx.strokeStyle = "#ffffff";
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.arc(legX + 20, legY + 38, 4.5, 0, Math.PI * 2);
    ctx.fill();
    ctx.stroke();

    ctx.fillStyle = isDark ? "#f8fafc" : "#0f172a";
    ctx.fillText("Empirical Seeds (N=330)", legX + 38, legY + 42);
  }

  window.redrawChangePoint = draw;
  resize();
}

/* Copy to Clipboard Utility */
function initCopyButtons() {
  document.querySelectorAll(".copy-btn").forEach((btn) => {
    btn.addEventListener("click", () => {
      const targetId = btn.getAttribute("data-target");
      const targetEl = document.getElementById(targetId);
      if (targetEl) {
        navigator.clipboard.writeText(targetEl.textContent.trim()).then(() => {
          const origText = btn.textContent;
          btn.textContent = "Copied!";
          setTimeout(() => {
            btn.textContent = origText;
          }, 2000);
        });
      }
    });
  });
}
