# lithography_sim
Personal project to simulate a pattern on a 2D material such as a silicon wafer. 
The principal objective of this project is to start by creating a very simple pattern on a simulated wafer.
After completing this step I'm gonna be updating the project to make it more user friendly and making it as personificable as it can be so each diferent user can
simulate its personal wafer with different patterns.
At some point I'm gonna be trying to print patterns designed by autoCAD to make this simulation as realistic as it can be. 

I also would like to implement a graphic interface to make it more easy to use.

Feel free to use this for your own projects but keep in mind I'm still a student and this is my first personal project and I'm very new at the semicons world and, to be fair, I'm also pretty new at coding :)

Little update about what I'm working on right now (not posted yet because I'm not having much free time and it's still in a very early stage):
Now that I've been able to make the simulation of the printing on the wafer I wanna work on how the laser affects it's printing.
To make this happen I'm working on a numerical algorithm that will have different parameters in consideration. The basic parameters that I'm working with are:

  -The properties of the mirror (material per example): 
    This parameter encompasses the material characteristics of the mirror, such as its reflectivity, thermal conductivity, and surface roughness. For instance, a         mirror with high reflectivity and low surface roughness ensures minimal scattering and energy loss, which is essential for maintaining the laser beam’s               integrity.  
    
  -The path the light will follow when reflecting on a mirror: 
    I am calculating the trajectory of the laser beam as it reflects off the mirror. By determining the angle between different reflection points, I can accurately       predict the beam's path. This is crucial for aligning the laser precisely on the wafer, ensuring that the printing process remains consistent and precise.
    
  -The momentum the photons will loose when geting reflexed on a mirror: 
    Although photons are massless, they carry momentum. When these photons reflect off a surface, their change in momentum results in a force (commonly referred to       as radiation pressure). Even though this force is generally very small, it might become significant in high-intensity applications or in extremely precise            setups. The momentum transfer can be estimated by considering the intensity of the laser and the reflection geometry.

I am trying to find the angle between two points to understand how the photons will act. As I said though, I still have a long journey ahead! I'm not very familiar with photonics, but I am sure enjoying this :) 

Clàudia Pàmies, UAB 
2024 
