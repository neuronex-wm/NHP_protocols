# NHP_protocols
Collection of protocols for recordings for the IRG2 Primate cell type database. The point of this repository is to facilitate and ensure standardized aquisition protocols.

Please make sure that the protocols you use are in line with the consesus template (see below) and upload these here. Only use the protocols uploaded here if you change your aquisition protocol update the respective file here.


Here is a preliminary working template based on protocols of the AIBS cell type database (see http://help.brain-map.org/download/attachments/8323525/CellTypes_Ephys_Overview.pdf?version=2&modificationDate=1508180425883&api=v2). Deviation are marked with ! . Please follow protocol name, order and variables as closly as possible/sensible given the differences in aquisition equipment:

The prestimulus intervall of all recorded protocol sweeps have the same structure containing a small and short hyperpolarizing test pulse:
40 ms 0 pA (no increment) Step \\ 10 ms -25 pA (no increment) Step \\ 450 ms 0 pA (no increment) Step

1. Ramp

3 repetetions of single sweep of (20 s 0-to-500 pA Ramp (slope: 25 pA/s) terminated manually after a series of action potentials are acquired) with an interstimulus\interrepettion intervall of >10 seconds.

2. Long Square Pulse

a) 1 repetetion of several sweeps of (1000 ms -105! pA (15! pA increment until supratheshold + 150/300! pA [depending on input resistance] are reached) Step \\  8500 ms 0 pA (0 pA increment) Step) \\ Start-to-Start Interval: 12! sec
b) 2-3 (Depending if 2a contains a sweep with a single spike = rheobase) repetetion of a single sweep of (1000 ms rheobase level pA Step \\ 8500 ms -105! pA (15! pA increment) Step 

3. Short Square Pulse

a) 1 repetetion of several sweeps of (3 ms 100 pA (10 pA increment) Step \\  1497 ms 0 pA (0 pA increment) Step)  \\ Start-to-Start Interval: 4 sec
b) at least 3 more repetitions of a single sweep of (3 ms first supratreshold level  Step \\  1497 ms 0 pA (0 pA increment) Step) \\ Start-to-Start Interval: 5 sec
c) if 3b did not produce an action potential at every repetition repeat 3b with 10 pA higher current step
