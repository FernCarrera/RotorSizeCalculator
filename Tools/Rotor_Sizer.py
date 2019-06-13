from __future__ import division

import numpy as np
import matplotlib.pyplot as plt
# Fernando Carrera
# IMPROVEMENTS TO MAKE:
# Need to write power function that includes voltage & Current

def findRadius(mass,props,diskAF,solidity,cd0,machTip):
    r = 0.1
    
    m = mass    #[kg]
    W = m*9.81  #[kg]
    nProp = props  #number of propellers
    rho = 1.225

    n = 1 #nProp/(nProp-2)  # Fail loading 1.33 n/(n-2), n = # of motors
    k = diskAF # effective disk area factor/ induced power correction factor
    sigma = solidity # solidity
    cdo = cd0
    m_tip = machTip
    T = W/nProp    # thrust for hover  
    T_max = T*n    # Max Thrust

    radius = []
    power = []
    fmerit = []
    DL = []
    Omega = []
  
    while r < 3:
        
        # Disk area
        S = np.pi*(r**2)
        
   
        # 1.7 is vahana T/W to handle rotor out with manuever
        tip_speed = 340*m_tip/np.sqrt(n)
        
        # RPM
        omega = (30/np.pi)*tip_speed/r

        # thrust coefficient
        ct = T/( rho * S* (tip_speed**2) )
        ct_max = T_max/( rho * S * (tip_speed**2) )

        # power coefficients
        cp_meas = ( k*( (ct**(3/2)) /np.sqrt(2)) + (1/8)*sigma*cdo )
        cp_meas_max = ( k*( (ct_max**(3/2)) /np.sqrt(2) ) + (1/8)*sigma*cdo )
        
       
        #power calculations
        P_shaft = (cp_meas_max*rho*S*(tip_speed**3))
        P_hover = (cp_meas*rho*S*(tip_speed**3))
        P_ideal = (T * np.sqrt(T/(2*S*rho)))

       
        # figure of merit
        F_merit = P_ideal/P_hover
        dl = T/(S*9.81)

        # saving data
        fmerit.append(F_merit)
        DL.append(dl)
        power.append(nProp*P_shaft/1000)
        radius.append(r)
        Omega.append(omega)
        r += 0.01
    print("Configuration Parameters:")
    print(" ")
    print("Mass",mass,"# Props:",props,"Disk Area Factor:",diskAF,"Solidity",solidity,'cd0:',cd0,"Tip Mach Speed",machTip)
    fig,((one,two),(three,four)) = plt.subplots(2,2)
    one.grid(True)
    two.grid(True)
    three.grid(True)
    four.grid(True)
    one.plot(radius,power)
    #one.plot(radius,fmerit)
    one.set_xlabel('Radius [m]')
    one.set_ylabel('Shaft Power [kW]')
    one.set_ylim(0,3000)
    one.set_title('Shaft Power vs. radius. ')
    two.plot(radius,Omega)
    #two.plot(radius,fmerit)
    two.set_xlabel('Radius [m]')
    two.set_ylabel('RPM')
    two.set_title('RPM vs Radius')
    two.set_ylim(0,5000)
    three.plot(radius,fmerit)
    three.set_xlabel('Radius [m]')
    three.set_ylabel('Figure of merit ')
    #three.set_title('rad v merit')
    four.plot(radius, DL)
    four.set_xlabel('Radius [m]')
    four.set_ylabel('Disc Loading in Thrust/Area')
    four.set_ylim(0,500)
    #four.set_title('rad v Ct')
    plt.show()
   
    return 
        


#if __name__ == "__main__":
    #radius,power,DL,fmerit,Omega = findRadius(2500,8,1.15,0.1,0.015,0.55)

    #fig,((one,two),(three,four)) = plt.subplots(2,2)
    #one.grid(True)
    #two.grid(True)
    #three.grid(True)
    #four.grid(True)
    #one.plot(radius,power)
    #one.plot(radius,fmerit)
    #one.set_xlabel('Radius [m]')
    #one.set_ylabel('Shaft Power [kW]')
    #one.set_ylim(0,3000)
    #one.set_title('Shaft Power vs. radius. ')
    #two.plot(radius,Omega)
    #two.plot(radius,fmerit)
    #two.set_xlabel('Radius [m]')
    #two.set_ylabel('RPM')
    #two.set_title('RPM vs Radius')
    #two.set_ylim(0,5000)
    #three.plot(radius,fmerit)
    #three.set_xlabel('Radius [m]')
    #three.set_ylabel('Figure of merit ')
    #three.set_title('rad v merit')
    #four.plot(radius, DL)
    #four.set_xlabel('Radius [m]')
    #four.set_ylabel('Disk Loading in Thrust/Area')
    #four.set_ylim(0,500)
    #four.set_title('rad v Ct')
    #plt.show()

    #print(fmerit)
    #print(ct)
