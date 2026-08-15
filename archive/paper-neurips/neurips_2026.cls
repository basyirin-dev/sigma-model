% ======================================================================
% neurips_2026.cls — Minimal stub for drafting
% FIXME: Replace with official class file from
%   https://media.neurips.cc/Conferences/NeurIPS2026/Styles/neurips_2026.sty
% when available.
% ======================================================================
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{neurips_2026}[2026/01/01 NeurIPS 2026 draft stub]

% --- Pass unknown options to article ---
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions\relax

% --- Base class ---
\LoadClass[10pt,twocolumn,letterpaper]{article}

% --- Paper geometry ---
\RequirePackage[letterpaper,margin=1in,headsep=0.25in,footskip=0.25in]{geometry}

% --- Font ---
\RequirePackage[T1]{fontenc}
\RequirePackage{times}
\RequirePackage{microtype}

% --- Section headings ---
\renewcommand{\section}{\@startsection{section}{1}{\z@}%
  {-3.5ex \@plus -1ex \@minus -.2ex}%
  {2.3ex \@plus .2ex}%
  {\normalfont\large\bfseries}}
\renewcommand{\subsection}{\@startsection{subsection}{2}{\z@}%
  {-3.25ex\@plus -1ex \@minus -.2ex}%
  {1.5ex \@plus .2ex}%
  {\normalfont\normalsize\bfseries}}
\renewcommand{\subsubsection}{\@startsection{subsubsection}{3}{\z@}%
  {-3.25ex\@plus -1ex \@minus -.2ex}%
  {1.5ex \@plus .2ex}%
  {\normalfont\normalsize\itshape}}

% --- Title ---
\renewcommand{\maketitle}{%
  \twocolumn[%
    \centering
    \LARGE\bfseries \@title \par
    \vskip 1.5em
    \normalsize \@author \par
    \vskip 1em
  ]%
}

% --- Abstract ---
\renewenvironment{abstract}{%
  \section*{\centering\small Abstract}%
  \small\itshape
}{%
  \par\medskip
}

% --- Bibliography ---
\RequirePackage{natbib}
\renewcommand{\bibsection}{\section*{References}}

\endinput
