# -*- coding: utf-8 -*-
"""
    pygments.lexers.chuck
    ~~~~~~~~~~~~~~~~~~~

    Pygments lexers for ChucK audio programming language.

    :copyright: Copyright 2006-2013 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import re

from pygments.lexer import Lexer, RegexLexer, include, bygroups, using, \
     this
from pygments.token import Text, Comment, Operator, Keyword, Name, String, \
     Number, Punctuation
from pygments.util import get_choice_opt
from pygments import unistring as uni


__all__ = ['ChucKLexer']


class ChucKLexer(RegexLexer):
    """
    For `ChucK <http://chuck.stanford.edu/>`_ source code.
    """

    name = 'ChucK'
    aliases = ['chuck', 'Chuck']
    filenames = ['*.ck']
    mimetypes = ['text/plain']

    flags = re.MULTILINE | re.DOTALL

    defaultClasses = [
        "Object",
        "string",
        "UAnaBlob",
        "Shred",
        "Thread",
        "Class",
        "Event",
        "IO",
        "FileIO",
        "StdOut",
        "StdErr",
        "Windowing",
        "Machine",
        "Std",
        "KBHit",
        "ConsoleInput",
        "StringTokenizer",
        "Math",
        "OscSend",
        "OscEvent",
        "OscRecv",
        "MidiMsg",
        "MidiIn",
        "MidiOut",
        "MidiRW",
        "MidiMsgIn",
        "MidiMsgOut",
        "HidMsg",
        "Hid",
    ]
    
    defaultUGens = [
        "UGen",
        "UAna",
        "Osc",
        "Phasor",
        "SinOsc",
        "TriOsc",
        "SawOsc",
        "PulseOsc",
        "SqrOsc",
        "GenX",
        "Gen5",
        "Gen7",
        "Pan2",
        "Gen9",
        "Gen10",
        "Gen17",
        "CurveTable",
        "WarpTable",
        "Chubgraph",
        "Chugen",
        "UGen_Stereo",
        "UGen_Multi",
        "DAC",
        "ADC",
        "Mix2",
        "Gain",
        "Noise",
        "CNoise",
        "Impulse",
        "Step",
        "HalfRect",
        "FullRect",
        "DelayP",
        "SndBuf",
        "SndBuf2",
        "Dyno",
        "LiSa",
        "FilterBasic",
        "BPF",
        "BRF",
        "LPF",
        "HPF",
        "ResonZ",
        "BiQuad",
        "Teabox",
        "StkInstrument",
        "BandedWG",
        "BlowBotl",
        "BlowHole",
        "Bowed",
        "Brass",
        "Clarinet",
        "Flute",
        "Mandolin",
        "ModalBar",
        "Moog",
        "Saxofony",
        "Shakers",
        "Sitar",
        "StifKarp",
        "VoicForm",
        "FM",
        "BeeThree",
        "FMVoices",
        "HevyMetl",
        "PercFlut",
        "Rhodey",
        "TubeBell",
        "Wurley",
        "Delay",
        "DelayA",
        "DelayL",
        "Echo",
        "Envelope",
        "ADSR",
        "FilterStk",
        "OnePole",
        "TwoPole",
        "OneZero",
        "TwoZero",
        "PoleZero",
        "JCRev",
        "NRev",
        "PRCRev",
        "Chorus",
        "Modulate",
        "PitShift",
        "SubNoise",
        "WvIn",
        "WaveLoop",
        "WvOut",
        "WvOut2",
        "BLT",
        "BlitSquare",
        "Blit",
        "BlitSaw",
        "JetTabl",
        "Mesh2D",
        "FFT",
        "IFFT",
        "Flip",
        "pilF",
        "DCT",
        "IDCT",
        "FeatureCollector",
        "Centroid",
        "Flux",
        "RMS",
        "RollOff",
        "AutoCorr",
        "XCorr",
        "ZeroX",
    ]

    tokens = {
        'root': [
            # method names
            (r'^(\s*(?:[a-zA-Z_][a-zA-Z0-9_\.\[\]<>]*\s+)+?)' # return arguments
             r'([a-zA-Z_][a-zA-Z0-9_]*)'                      # method name
             r'(\s*)(\()',                                    # signature start
             bygroups(using(this), Name.Function, Text, Operator)),
            (r'[^\S\n]+', Text),
            (r'//.*?\n', Comment.Single),
            (r'/\*.*?\*/', Comment.Multiline),
            (r'(break|continue|do|else|for|'
             r'dur|time|string'
             r'if|new|return|spork|switch|this|while)\b',
             Keyword),
            (r'(const|extends|fun|function|public|static)\b', Keyword.Declaration),
            (r'(float|int|void|complex|polar|dur|time)\b',
             Keyword.Type),
            (r'(true|false|maybe|null|pi|samp|ms|second|minute|hour|day|week|now|adc|dac|blackhole|me)\b', Keyword.Constant),
            (r'(class)(\s+)', bygroups(Keyword.Declaration, Text), 'class'),
            (r'(%s)' % '|'.join(defaultClasses + defaultUGens), Name.Builtin), 
            (r'"(\\\\|\\"|[^"])*"', String),
            (r"'\\.'|'[^\\]'|'\\u[0-9a-fA-F]{4}'", String.Char),
            (r'(\.)([a-zA-Z_][a-zA-Z0-9_]*)', bygroups(Operator, Name.Attribute)),
            (r'[a-zA-Z_][a-zA-Z0-9_]*:', Name.Label),
            (r'[a-zA-Z_\$][a-zA-Z0-9_]*', Name),
            (r'[~\^\*!%&\[\]\(\)\{\}<>\|+=:;,./?-]', Operator),
            (r'[0-9][0-9]*\.[0-9]+([eE][0-9]+)?[fd]?', Number.Float),
            (r'0x[0-9a-fA-F]+', Number.Hex),
            (r'[0-9]+L?', Number.Integer),
            (r'\n', Text)
        ],
        'class': [
            (r'[a-zA-Z_][a-zA-Z0-9_]*', Name.Class, '#pop')
        ],
    }
