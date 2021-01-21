# NHP_protocols
Collection of protocols for recordings for the IRG2 Primate cell type database. The point of this repository is to facilitate and ensure standardized aquisition protocols.

Please make sure that the protocols you use are in line with the consesus template (see below) and upload these here. Only use the protocols uploaded here if you change your aquisition protocol update the respective file here.


Here is a preliminary working template based on protocols of the first batch of the AIBS cell type database (see http://help.brain-map.org/download/attachments/8323525/CellTypes_Ephys_Overview.pdf?version=2&modificationDate=1508180425883&api=v2 in the section Appendix: Stimulus Details). 
  Deviation are marked with ! . Please follow protocol name, order and variables as closly as possible/sensible given the differences in aquisition equipment:

Different "stimulus segments"/epoches are separated by "\\". 


**0. General features** 

  __**a.** The prestimulus intervall of all recorded sweeps should have the same structure including a small and short hyperpolarizing! test pulse: <br />
     40 ms 0 pA Step (no increment over sweeps) \\ 10 ms -25 pA Step (no increment over sweeps)  \\ 450 ms 0 pA Step  (no increment over sweeps) <br />

  __**b.** Sampling frequency for continous amplifiers is 50kHz. In discontinous amplifiers as high as sensible/possible (at least 25kHz)! <br /> 
  
  __**c.** except when measuring the membrane potential within the first minute(s) after breakthrough, a holding current is applied to keep the baseline from drifting. The readjustment can be done either manually or automatically using algorithms as provided in MIES.

**1. Ramp**

  __**a.** 3 repetetions of single sweep of \\ 20 s 0-to-500 pA Ramp (slope: 25 pA/s) terminated manually after a series of action potentials are acquired) with an 
     interstimulus\interrepettion intervall of >10 seconds.

**2. Long Square Pulse**

   __**a.** 1 repetetion of sweeps \\ 1000 ms Step of -110 pA (+20 pA increment over sweeps until supratheshold level + 160 are reached)  \\  6500 ms  0 pA Step (no increment over sweeps) <br />  Start-to-Start Interval: 10 sec for all! AIBS actually uses 10 sec for subthreshold 17 sec for suprathreshold, but imho too complex for now <br />  Side notes: in rare cases with very low input resistance they start at -190 or -210 with a higher current increment  <br /> upper limit of current injections should depend on input resistance of the cell; most basket cells should be able to take  supratheshold level + 300 pA.
  __**b.** 2-3 repetetion of a single sweep of \\ 1000 ms "rheobase" level pA Step  \\  6500 ms  0 pA Step (no increment over sweeps) <br />  Side note:The AIBS makes sure that they have 3 repetetions of the "rheobase" level spike for each cell. How many extra sweeps depends on if 2a contains a sweep with a single spike or something close to it (some times not possible if intrinsic bursting etc.), which technically is not the exact definitation of rheobase so it is in "" here.

**3. Short Square Pulse**

  __**a.** 1 repetetion of several sweeps of (3 ms 100 pA (10 pA increment) Step \\  1497 ms 0 pA (0 pA increment) Step)  \\ Start-to-Start Interval: 4 sec; AIBS actually uses 4 sec for subthreshold 5 sec for suprathreshold, but imho too complex for now <br /> 
  __**b.** at least 3 more repetitions of a single sweep of (3 ms first supratreshold level  Step \\  1497 ms 0 pA (0 pA increment) Step) \\ Start-to-Start Interval: 5 sec <br/>
 __**c.** if 3b did not produce an action potential at every repetition repeat 3b with 10 pA higher current step <br /> Side notes:
