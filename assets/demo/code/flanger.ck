SndBuf buffy => Gain direct => dac;
direct => Delay delayed => dac;

me.sourceDir() + "/geetar.wav" => buffy.read;
1::second => delayed.max;

SinOsc flangerLfo => blackhole;
0.5 => flangerLfo.freq;

2::ms => dur base;
1::ms => dur mod;
while(true)
{
    base + flangerLfo.last()*mod => delayed.delay;
    1::ms => now;
}
