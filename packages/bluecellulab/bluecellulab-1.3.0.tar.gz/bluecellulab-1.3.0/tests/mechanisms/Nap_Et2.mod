:Comment : mtau deduced from text (said to be 6 times faster than for NaTa)
:Comment : so I used the equations from NaT and multiplied by 6
:Reference : Modeled according to kinetics derived from Magistretti & Alonso 1999
:Comment: corrected rates using q10 = 2.3, target temperature 34, orginal 21

: Adapted by Werner Van Geit @ BBP, 2015 (with help from M.Hines):
: channel detects TTX concentration set by TTXDynamicsSwitch.mod

: LJP: OK, cell-attached modes bath and pipette solution almost identical ljp < 1mV "this procedure can be considered as valid in the case of a cell-attached or inside-out patch measurement provided that the pipette contains a solution identical to that of the bath" Erwin Neher, 1992


NEURON {
	SUFFIX Nap_Et2
	USEION na READ ena WRITE ina
	USEION ttx READ ttxo, ttxi VALENCE 1
	RANGE gNap_Et2bar, gNap_Et2, ina
}

UNITS	{
	(S) = (siemens)
	(mV) = (millivolt)
	(mA) = (milliamp)
}

PARAMETER	{
	gNap_Et2bar = 0.00001 (S/cm2)
}

ASSIGNED {
	ttxo (mM)
	ttxi (mM)
	v	(mV)
	ena	(mV)
	ina	(mA/cm2)
	gNap_Et2	(S/cm2)
	mInf
	mTau
	mAlpha
	mBeta
	hInf
	hTau
	hAlpha
	hBeta
}

STATE	{
	m
	h
}

BREAKPOINT	{
	SOLVE states METHOD cnexp
	gNap_Et2 = gNap_Et2bar*m*m*m*h
	ina = gNap_Et2*(v-ena)
}

DERIVATIVE states	{
	if (ttxi == 0.015625 && ttxo > 1e-12) {
		mInf = 0.0
		mTau = 1e-12
		hInf = 1.0
		hTau = 1e-12
	} else {
		rates()
	}
	m' = (mInf-m)/mTau
	h' = (hInf-h)/hTau
}

INITIAL{
	if (ttxi == 0.015625 && ttxo > 1e-12) {
		mInf = 0.0
		mTau = 1e-12
		hInf = 1.0
		hTau = 1e-12
	} else {
		rates()
	}
	m = mInf
	h = hInf
}

PROCEDURE rates(){
  LOCAL qt
  qt = 2.3^((34-21)/10)

	UNITSOFF
		mInf = 1.0/(1+exp((v- -52.6)/-4.6))
    if(v == -38){
    	v = v+0.0001
    }
		mAlpha = (0.182 * (v- -38))/(1-(exp(-(v- -38)/6)))
		mBeta  = (0.124 * (-v -38))/(1-(exp(-(-v -38)/6)))
		mTau = 6*(1/(mAlpha + mBeta))/qt

  	if(v == -17){
   		v = v + 0.0001
  	}
    if(v == -64.4){
      v = v+0.0001
    }

		hInf = 1.0/(1+exp((v- -48.8)/10))
    hAlpha = -2.88e-6 * (v + 17) / (1 - exp((v + 17)/4.63))
    hBeta = 6.94e-6 * (v + 64.4) / (1 - exp(-(v + 64.4)/2.63))
		hTau = (1/(hAlpha + hBeta))/qt
	UNITSON
}
