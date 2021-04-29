! ***********************************************************************
!
!   Copyright (C) 2010  Bill Paxton
!
!   this file is part of mesa.
!
!   mesa is free software; you can redistribute it and/or modify
!   it under the terms of the gnu general library public license as published
!   by the free software foundation; either version 2 of the license, or
!   (at your option) any later version.
!
!   mesa is distributed in the hope that it will be useful, 
!   but without any warranty; without even the implied warranty of
!   merchantability or fitness for a particular purpose.  see the
!   gnu library general public license for more details.
!
!   you should have received a copy of the gnu library general public license
!   along with this software; if not, write to the free software
!   foundation, inc., 59 temple place, suite 330, boston, ma 02111-1307 usa
!
! ***********************************************************************

!==================================================================================
!
! Description here: 
! 
! Zsolt Keszthelyi et al. 
!
!==================================================================================
module run_star_extras

  use const_lib
  use const_def      
  use star_private_def  ! THIS ALWAYS HAS TO BE COPIED MANUALLY AFTER NEW INSTALLATION! it is in star/make and has to be in ../include
  use star_lib
  use star_def
  use chem_def, only: ih1, ihe4, ic12, ic13, in14, io16

  implicit none

      ! Module variables: 
      !==========================
      real(dp) :: R_init  ! initial radius, calc. actual value in mag routine
      real(dp) :: vesc    ! escape velocity (calculated for electron scattering opacity)
      real(dp) :: vinf    ! terminal velocity
      real(dp) :: Gamma_e  ! Gamma_e is the Eddington factor for electron scattering  
      real(dp) :: f_rot     ! rotational enhancement following Maeder & Meynet (2000)
      real(dp) :: Mdot_orig ! original mass-loss rate 
      real(dp) :: w_wlr     ! WLR rates
      real(dp) :: w_vink01
      integer  :: use_w_vink01
      real(dp) :: w_vink18
      integer  :: use_w_vink18      
      real(dp) :: w_graefener
      real(dp) :: w_vanloon
      real(dp) :: w_dejager
      real(dp) :: w_beasor
      integer  :: use_w_beasor      
      real(dp) :: w_kee
      integer  :: use_w_kee      
      real(dp) :: w_leuven
      integer  :: use_w_leuven      
      real(dp) :: w_krticka
      integer  :: use_w_krticka      
      real(dp) :: w_sander
      integer  :: use_w_sander      
      real(dp) :: WLR_alpha ! alpha 
      real(dp) :: WLR_logD0 ! logD0 - offset of the WLR
      real(dp) :: core_h1_init  ! initial core H content
      integer, parameter :: route1 = 1    ! vink01 + beasor + sander 
      integer, parameter :: route2 = 2    ! vink18 + beasor + sander 
      integer, parameter :: route3 = 3    ! leuven + beasor + sander 
      integer, parameter :: route4 = 4    ! krticka + beasor + sander 
      integer, parameter :: route5 = 5    !  vink01 + kee + sander 
      integer, parameter :: route6 = 6    !  vink18 + kee + sander 
      integer, parameter :: route7 = 7    !  leuven + kee + sander 
      integer, parameter :: route8 = 8    !  krticka + kee + sander 
      integer, parameter :: route9 = 9    !  wlr
      integer, save  :: windscheme = 0    ! wind scheme 
      !==========================

 contains
      
  subroutine extras_controls(id, ierr)

    integer, intent(in) :: id
    integer, intent(out) :: ierr
    
    type (star_info), pointer :: s

    ierr = 0

    call star_ptr(id, s, ierr)
    if (ierr /= 0) return

    s% extras_startup => extras_startup
    s% extras_check_model => extras_check_model
    s% extras_finish_step => extras_finish_step
    s% extras_after_evolve => extras_after_evolve
    s% how_many_extra_history_columns => how_many_extra_history_columns
    s% data_for_extra_history_columns => data_for_extra_history_columns
    s% how_many_extra_profile_columns => how_many_extra_profile_columns
    s% data_for_extra_profile_columns => data_for_extra_profile_columns  

    s% other_wind => THE_WIND     ! wind routines

    ! Once you have set the function pointers you want,
    ! then uncomment this (or set it in your star_job inlist)
    ! to disable the printed warning message,

    s% job% warn_run_star_extras =.false.       
    
    ! ====================================================
    ! 
    ! ====================================================

    if (s%job%extras_lrpar >= 1) then
       WLR_alpha = s%job%extras_rpar(1)
       WLR_logD0 = s%job%extras_rpar(2)
    else
       stop 'Initial parameters are not set using extras_rpar()'
    endif

    if (s%job%extras_lcpar >= 1) then

       select case (s%job%extras_cpar(1))
       case ('route1')
          windscheme = route1
       case ('route2')
          windscheme = route2
       case ('route3')
          windscheme = route3
       case ('route4')
          windscheme = route4
       case ('route5')
          windscheme = route5
       case ('route6')
          windscheme = route6
       case ('route7')
          windscheme = route7
       case ('route8')
          windscheme = route8
       case ('route9')
          windscheme = route9
       case default
          stop 'Wind scheme is not set.'
       end select

    endif 
            
  end subroutine extras_controls

 ! ====================================================     
 
  subroutine extras_startup(id, restart, ierr)
         type (star_info), pointer :: s
         integer, intent(in) :: id
         logical, intent(in) :: restart
         integer, intent(out) :: ierr
         integer :: h1
         ierr = 0
         call star_ptr(id, s, ierr)
         call get_star_ptr(id,s,ierr)

         ! Usual startup stuff
         if (.not. restart) then
            call alloc_extra_info(s)
         else ! it is a restart
            call unpack_extra_info(s)
         end if
         
         ! Store the initial H core mass fraction
         ! This will be used to calculate the ZAMS radius 
         ! for magnetic flux conservation
         !
          h1 = s% net_iso(ih1)
          core_h1_init = s% xa(h1,s% nz)

          R_init = 0.0d0 !!  R_init is set to zero for the first model. 
                         !! it is then calculated in the magnetic routine.

          WRITE (*,*) '======================================================='
          WRITE (*,*) 'Chosen route of wind scheme '
          WRITE (*,*)  windscheme
          WRITE (*,*) '======================================================='

      end subroutine extras_startup

  ! ====================================================
  
      ! returns either keep_going, retry, or terminate.
      integer function extras_check_model(id)
         integer, intent(in) :: id
         integer :: ierr
         type (star_info), pointer :: s
         ierr = 0
         call star_ptr(id, s, ierr)
         if (ierr /= 0) return
         extras_check_model = keep_going         
         !if (.false. .and. s% star_mass_h1 < 0.35d0) then
            ! stop when star hydrogen mass drops to specified level
         !   extras_check_model = terminate
         !   write(*, *) 'have reached desired hydrogen mass'
         !   return
         !end if  ! was this supposed to be default???
         ! by default, indicate where (in the code) MESA terminated
         if (extras_check_model == terminate) s% termination_code = t_extras_check_model
      end function extras_check_model
  !****

  !****

  integer function extras_finish_step(id)
    integer, intent(in) :: id
    integer :: ierr
    integer :: h1 
    real(dp) :: core_h1
    type (star_info), pointer :: s 

    ierr = 0
    call star_ptr(id, s, ierr)
    if (ierr /= 0) return
    
    extras_finish_step = keep_going
    call store_extra_info(s)
    
   !! ======= Profile for models at any custom time ==========
   ! if (s% star_age >= 0.999d6 .AND. s% star_age < 1.001d6) then
   !  call star_write_profile_info(s% id, 'LOGS/prof1Myr.data', s% id, ierr) 
   !  WRITE(*,*) 'A structure profile is saved.'
   ! end if
   
   h1 = s% net_iso(ih1)
   core_h1 = s% xa(h1,s% nz)
   
   !! ======= Profile for models at any custom X_c ==========
    if (core_h1 <= (core_h1_init * 0.997d0) .AND. core_h1 > (core_h1_init * 0.991d0)) then
     call star_write_profile_info(s% id, 'LOGS/prof_ZAMS.data', ierr) 
     WRITE(*,*) 'A structure profile is saved.'
    end if
    if (core_h1 <= (core_h1_init * 0.51d0) .AND. core_h1 > (core_h1_init * 0.49d0)) then
     call star_write_profile_info(s% id, 'LOGS/prof_midMS.data', ierr) 
     WRITE(*,*) 'A structure profile is saved.'
    end if
     if (core_h1 <= (core_h1_init * 0.09d0) .AND. core_h1 > (core_h1_init * 0.009d0)) then
     call star_write_profile_info(s% id, 'LOGS/prof_TAMS.data', ierr) 
     WRITE(*,*) 'A structure profile is saved.'
    end if   
    ! see extras_check_model for information about custom termination codes
    ! by default, indicate where (in the code) MESA terminated
    if (extras_finish_step == terminate) s% termination_code = t_extras_finish_step

  end function extras_finish_step

!=========================================================
!!!! ******** Main additions from here *******************
!
! Note that since we need vinf, we calculate it explicitly from 
! the Eddington parameter for pure electron scattering.
! We also adopt the bi-stability, that is the behaviour of vinf/vesc. and Mdot at a given Teff.
! This should be carefully checked to be consistent with the wind description.

! === Terminal velocity using Gamma for electron scattering (Kudritzki et al. 1986)=== 
! === Rotational enhancement following Maeder & Meynet (2000) === 
! 
! gammae routine based on the implementation of 
! Keszthelyi, Puls, Wade, 2017, A&A 584, A4 (KPW2017)
!
subroutine gammae(id,ierr)
  type (star_info), pointer :: s
  integer, intent(in) :: id
  integer, intent(out) :: ierr
  integer :: h1, he4, nz
  real(dp) :: alfa1, alfa2, L1, M1, T1, R1 ! alfa1,2 used for interpolation only
  real(dp) :: I_he, YHe, sigma_e 
  real(dp) :: vinf1, vinf2, vinf3, logvinf 
  real(dp) :: surface_h1, surface_he4   
  real(dp) :: nom, denom, powe
  real(dp) :: f_rot1, f_rot2, f_rot3
  real(dp) :: X, Y, Z  ! H, He and metal mass fractions
  real(dp) :: alpha  ! force multiplier parameter with simple Teff dependence - new - 
! --- Values related to the bi-stability --- check consistency with wind routine!

! The calculations are partitioned into three Teff regimes. 
  real(dp), parameter :: Teff_jump1 = 20.d3   ! Revised bi-stability jump temperature. See Petrov, et al. (2016), 
                                              ! KPW2017, and Vink (2018).
! FIRST bi-stability jump temperature (from observations)
  real(dp), parameter :: Teff_jump2 = 10.d3  
! SECOND bi-stability jump temperature (from observations) 
  real(dp), parameter :: dT1 = 1.d3   ! adopted for consistency with Vink routine
! Interpolation width of the first bi-stability jump. 
! Note that a small dT results in a steep change
! in Mdot while a larger dT yields a more gradual change. 
  real(dp), parameter :: dT2 = 1.d3   ! second jump 
! Interpolation width of the second bi-stability jump. 

! --- Values related to terminal wind velocity ---
! adopted from Kudritzki & Puls (2000), ARA&A, 38, 613; and Markova & Puls (2008), A&A, 478, 823
  real(dp), parameter :: fvinf1 = 2.6d0  ! ratio of terminal to escape velocity before Teff_jump_1
  real(dp), parameter :: fvinf2 = 1.3d0  ! ratio of terminal to escape velocity after Teff_jump_1 and before Teff_jump_2
  real(dp), parameter :: fvinf3 = 0.7d0  ! ratio of terminal to escape velocity after Teff_jump_2

  call get_star_ptr(id,s,ierr)

  L1 = s% photosphere_L         ! cgs
  M1 = s% star_mass * Msun      ! cgs
  T1 = s% Teff                  ! cgs
  R1 = s% photosphere_r * Rsun  ! cgs

!--- elements ---- 
  nz = s% nz
  h1 = s% net_iso(ih1)
  he4 = s% net_iso(ihe4)
  surface_h1 = s% xa(h1,1)
  surface_he4 = s% xa(he4,1)
  X = surface_h1            ! mass fraction of H
  Y = surface_he4           ! mass fraction of He
  Z = 1.d0 - (X + Y)        ! surface metallicity 

  YHe = Y/X / 4.d0  
! surface Helium content by number, 
! n_He/n_H; approximation: factor 4 should be m_He/m_H

! === PATH 1 === 
  ! --- vinf behaviour --- check for consistency with wind routine 
 if (T1 .ge. Teff_jump1 - dT1) then 
    I_he = 2.d0  ! the number of free electrons per He nuclei (hot regime)
    sigma_e = 0.398d0 * (1.d0 + YHe * I_he) / (1.d0 + 4.d0 * YHe)  ! Eq. 66 by Kudritzki et al. (1989) A&A, 219, 205 
    Gamma_e =  sigma_e * L1/(M1 * pi4 * standard_cgrav * clight) 
! escape velocity corrected for electron scattering 
    vesc = sqrt((1.d0 - Gamma_e) * 2.d0 * standard_cgrav * M1 / R1 )
! Eq. 15 KPW2017
    vinf1 = vesc * fvinf1
    vinf = vinf1
! rotational enhancement 
    alpha = 0.6 ! set to 0.6 for path 1 
    nom = 1.d0 - Gamma_e
    denom = 1.d0 - (4.d0/9.d0 * pow(s%v_rot_avg_surf / s%v_crit_avg_surf, 2.0d0) ) - Gamma_e  ! Note vit definition is different! 
    powe = (1.d0 / alpha) - 1.d0
    f_rot1 = pow(nom, powe) / pow(denom, powe)  
    f_rot = f_rot1
endif
! === PATH 2 === 
 if (T1 .le. Teff_jump1 + dT1 .and. T1 .ge. Teff_jump2 - dT2) then 
    I_he = 1.d0     ! cooler side of jump, Helium recombined to HeII 
    sigma_e = 0.398d0 * (1.d0 + YHe * I_he) / (1.d0 + 4.d0 * YHe)  
    Gamma_e =  sigma_e * L1/(M1 * pi4 * standard_cgrav * clight) 
    vesc = sqrt(2.d0 * standard_cgrav * M1 / R1 * (1.d0-Gamma_e))
    vinf2 = vesc * fvinf2
    vinf = vinf2
! rotational enhancement 
    alpha = 0.5 ! set for path 2
    nom = 1.d0 - Gamma_e
    denom = 1.d0 - (4.d0/9.d0 * pow(s%v_rot_avg_surf / s%v_crit_avg_surf, 2.0d0) ) - Gamma_e  
    powe = (1.d0 / alpha) - 1.d0
    f_rot2 = pow(nom, powe) / pow(denom, powe) 
    f_rot = f_rot2
 endif
! --- INTERPOLATION for the FIRST bi-stability jump ---  
 if (Teff_jump1 + dT1 > T1 .and. T1 > Teff_jump1 - dT1) then
    alfa1 = (T1 - (Teff_jump1 - dT1)) / (2.d0 * dT1)
    vinf = alfa1 * vinf1 + (1.d0 - alfa1) * vinf2
    f_rot = alfa1 * f_rot1 + (1.d0 - alfa1) * f_rot2
 endif
! === PATH 3 ===
 if (T1 .le. Teff_jump2 + dT2) then
    sigma_e = 0.398d0 * 1.d0 / (1.d0 + 4.d0 * YHe) ! since I_he = 0 for T1 < 10 kK. 
    Gamma_e =  sigma_e * L1/(M1 * pi4 * standard_cgrav * clight) 
    vesc = sqrt(2.d0 * standard_cgrav * M1 / R1 * (1.d0-Gamma_e))   
    vinf3 = vesc * fvinf3
    vinf = vinf3
! rotational enhancement 
    alpha = 0.4
    nom = 1.d0 - Gamma_e
    denom = 1.d0 - (4.d0/9.d0 * pow(s%v_rot_avg_surf / s%v_crit_avg_surf, 2.0d0) ) - Gamma_e  
    powe = (1.d0 / alpha) - 1.d0
    f_rot3 = pow(nom, powe) / pow(denom, powe) 
    f_rot = f_rot3
 endif
! --- INTERPOLATION for the SECOND bi-stability jump ---    
 if (Teff_jump2 + dT2 > T1 .and. T1 > Teff_jump2 - dT2) then
    alfa2 = (T1 - (Teff_jump2 - dT2)) / (2.d0 * dT2)  
    vinf = alfa2 * vinf2 + (1.d0 - alfa2) * vinf3
    f_rot = alfa2 * f_rot2 + (1.d0 - alfa2) * f_rot3
 endif

! To avoid numerical problems, if f_rot is too small (or rotation is very slow), 
! just ignore the rotational enhahncement on the mass-loss rates. 

if (f_rot .le. 1.d-4 .OR. s%v_rot_avg_surf .le. 1.d0) then   
    f_rot = 1.d0
endif 

end subroutine gammae


! ========================================
!      === FINAL WIND SCHEMES AND ===
!      === ROTATIONAL ENHANCEMENT === 
! ========================================

subroutine THE_WIND(id, Lsurf, Msurf, Rsurf, Tsurf, X, Y, Z, w, ierr)
  type (star_info), pointer :: s
  real(dp), intent(in) :: Lsurf, Msurf, Rsurf, Tsurf, X, Y, Z ! surface values (cgs)
   integer, intent(out) :: ierr
  integer ::  h1, he4, nz
  real(dp) :: surface_h1, surface_he4, T1, L1, M1, R1
  integer, intent(in) :: id
  real(dp), intent(out) :: w
  logical, parameter :: dbg = .false.
  real(dp), parameter :: Tint= 10.e3 ! temperature to switch winds with interpolation
  real(dp), parameter :: dT = 1.d3   ! interpolation range in Teff 
  real(dp), parameter :: Xint= 0.3d0 ! surface hydrogen content to switch winds with interpolation
  real(dp), parameter :: dX = 0.03d0 ! interpolation range in surface hydrogen content
  real(dp) :: alfaint, logMdot1, logMdot2, logMdot3, logMdot4
  real(dp) :: exp1, exp2
  real(dp), parameter :: Zsolar1 = 0.019d0 ! value used by Vink 
  real(dp), parameter :: Zsolar2 = 0.013d0 ! value used by Sundqvist, Bjorklund 
  
  include 'formats'

  call get_star_ptr(id,s,ierr)  ! pointer to get data
  call gammae(id,ierr)    ! call for rotational boost on mass-loss rates 
  call Vink01(id, Lsurf, Msurf, Rsurf, Tsurf, X, Y, Z, w, ierr)
  call WWLR(id, Lsurf, Msurf, Rsurf, Tsurf, X, Y, Z, w, ierr)
  call Sander(id, Lsurf, Msurf, Rsurf, Tsurf, X, Y, Z, w, ierr)

  L1 = Lsurf   ! cgs
  M1 = Msurf   ! cgs
  T1 = Tsurf   ! cgs
  R1 = Rsurf

  nz = s% nz
  h1 = s% net_iso(ih1)
  he4 = s% net_iso(ihe4)
  surface_h1 = s% xa(h1,1)
  surface_he4 = s% xa(he4,1)

  ! winds  
  !=================================================================================
  ! rates from Vink 2018
  logMdot1 = - 9.13d0 + 2.1d0 * log10(M1/Msun) + 0.74d0 * log10(Z/Zsolar1)
  w_vink18 = exp10(logMdot1)
  ! Leuven rates from Sundqvist et al. 2019 and Bjorklund et al. 2020
  logMdot2 = - 5.55d0 + 0.79d0 * log10(Z/Zsolar2) + (2.16d0 - 0.32d0 * log10(Z/Zsolar2) ) * log10(L1/(10**6 * Lsun))
  w_leuven = exp10(logMdot2)
  ! Krticka et al. 2021
  exp1 = exp(-(T1-14.1d3)**2/4.88d3**2)  
  exp2 = exp(-(T1-37.3d3)**2/58.8d3**2)
  logMdot3 = - 24.228d0 + 1.50d0 * log10(1.e-6*L1/Lsun) + 24.228d0 * log10(exp1 + 5.82d0 * exp2)
  logMdot3 = logMdot3 + 0.85d0 * log10(Z/Zsolar2) ! Z-dependence set by Zsolt, assuming exponent and Zsolar2 
  w_krticka = exp10(logMdot3) !!! - log10(secyer) + log10(Msun))  
  ! Beasor, Davies, et al. 2020 MNRAS.492.5994B 
  logMdot4 = - 26.4d0 - (0.23d0 * M1/Msun) + 4.8d0 * log10(L1/Lsun) 
  w_beasor = exp10(logMdot4) ! Z-dependence not included for now
  !=================================================================================
 
 select case (windscheme)  ! set in inlist. 
!======== Vink, Lamers, de Koter 2000,20001, Beasor et al. 2020, Sander & Vink 2020 ===================================   
  case (route1)
! main route
   if (T1 .GE. Tint+dT .AND. X .GE. Xint+dX) then 
     Mdot_orig = w_vink01
     use_w_vink01 = 1  
   else 
     use_w_vink01 = 0  
   end if
   if (T1 <  Tint-dT) then 
     Mdot_orig = w_beasor
     use_w_beasor = 1
   else 
     use_w_beasor = 0 
   end if
   if (T1 .GE.  Tint+dT .AND. X < Xint-dX) then 
     Mdot_orig = w_sander
     use_w_sander = 1 
   else 
     use_w_sander = 0   
   end if
! interpolations 
   if (T1 < Tint+dT .AND. T1 > Tint - dT) then
    alfaint = (T1 - (Tint - dT)) / (2.d0 * dT)
    Mdot_orig = alfaint * w_vink01 + (1.d0 - alfaint) * w_beasor
   end if
   if (X < Xint + dX .AND. X > Xint - dX) then 
    alfaint = (X - (Xint - dX)) / (2.d0 * dX)
    Mdot_orig = alfaint * w_vink01 + (1.d0 - alfaint) * w_sander
   end if

!======= Vink 2018, Beasor et al. 2020, Sander & Vink 2020 ===================================   
  case (route2)
! main route
   if (T1 .GE. Tint+dT .AND. X .GE. Xint+dX) then 
      Mdot_orig = w_vink18
      use_w_vink18 = 1 
   else 
      use_w_vink18 = 0    
   end if
   if (T1 <  Tint-dT) then 
     Mdot_orig = w_beasor
     use_w_beasor = 1
   else 
     use_w_beasor = 0 
   end if
   if (T1 .GE.  Tint+dT .AND. X < Xint-dX) then 
     Mdot_orig = w_sander
     use_w_sander = 1 
   else 
     use_w_sander = 0   
   end if
! interpolations 
   if (T1 < Tint+dT .AND. T1 > Tint - dT) then
    alfaint = (T1 - (Tint - dT)) / (2.d0 * dT)
    Mdot_orig = alfaint * w_vink18 + (1.d0 - alfaint) * w_beasor
   end if
   if (X < Xint + dX .AND. X > Xint - dX) then 
    alfaint = (X - (Xint - dX)) / (2.d0 * dX)
    Mdot_orig = alfaint * w_vink18 + (1.d0 - alfaint) * w_sander
   end if

!======= Leuven (Sundqvist, Bjorklund 2019, 2020), Beasor et al. 2020, Sander & Vink 2020 ===================================   
  case (route3)
! main route
   if (T1 .GE. Tint+dT .AND. X .GE. Xint+dX) then 
      Mdot_orig = w_leuven
      use_w_leuven = 1 
   else 
      use_w_leuven = 0    
   end if
   if (T1 <  Tint-dT) then 
     Mdot_orig = w_beasor
     use_w_beasor = 1
   else 
     use_w_beasor = 0 
   end if
   if (T1 .GE.  Tint+dT .AND. X < Xint-dX) then 
     Mdot_orig = w_sander
     use_w_sander = 1 
   else 
     use_w_sander = 0   
   end if
! interpolations 
   if (T1 < Tint+dT .AND. T1 > Tint - dT) then
    alfaint = (T1 - (Tint - dT)) / (2.d0 * dT)
    Mdot_orig = alfaint * w_leuven + (1.d0 - alfaint) * w_beasor
   end if
   if (X < Xint + dX .AND. X > Xint - dX) then 
    alfaint = (X - (Xint - dX)) / (2.d0 * dX)
    Mdot_orig = alfaint * w_leuven + (1.d0 - alfaint) * w_sander
   end if

!======= Krticka et al. 2021, Beasor et al. 2020, Sander & Vink 2020 ===================================   
  case (route4)
! main route
   if (T1 .GE. Tint+dT .AND. X .GE. Xint+dX) then 
      Mdot_orig = w_krticka
      use_w_krticka = 1 
   else 
      use_w_krticka = 0    
   end if
   if (T1 <  Tint-dT) then 
     Mdot_orig = w_beasor
     use_w_beasor = 1
   else 
     use_w_beasor = 0 
   end if
   if (T1 .GE.  Tint+dT .AND. X < Xint-dX) then 
     Mdot_orig = w_sander
     use_w_sander = 1 
   else 
     use_w_sander = 0   
   end if
! interpolations 
   if (T1 < Tint+dT .AND. T1 > Tint - dT) then
    alfaint = (T1 - (Tint - dT)) / (2.d0 * dT)
    Mdot_orig = alfaint * w_krticka + (1.d0 - alfaint) * w_beasor
   end if
   if (X < Xint + dX .AND. X > Xint - dX) then 
    alfaint = (X - (Xint - dX)) / (2.d0 * dX)
    Mdot_orig = alfaint * w_krticka + (1.d0 - alfaint) * w_sander
   end if
!======================================================= 
   case default
    stop 'Wind is not okay.'
 end select  ! method

 ! ========================================
 ! === Final mass-loss rate of the star ===
 ! ========================================
if (f_rot > 0.d0) then 
  w = Mdot_orig * f_rot  ! scaled by rotational enhancement
 else 
  w = Mdot_orig 
  write(*,*) 'f_rot is zero. f_rot, Mdot_orig' 
  write(*,*)  f_rot, Mdot_orig
end if
  if (dbg) write(*,*) 'wind', w

end subroutine THE_WIND

! =====================


!--- MESA's default Vink01 routine (updated following KPW2017)  ---

subroutine Vink01(id, Lsurf, Msurf, Rsurf, Tsurf, X, Y, Z, w, ierr)

  type (star_info), pointer :: s
  real(dp), intent(in) :: Lsurf, Msurf, Rsurf, Tsurf, X, Y, Z ! surface values (cgs)
  integer, intent(in) :: id
  integer, intent(out) :: ierr
  integer :: h1, he4, nz
  real(dp) :: L1, M1, R1, T1, surface_h1, surface_he4
  logical, parameter :: dbg = .false.
  real(dp), intent(out) :: w
  real(dp) :: alfa, w1a, w2a, w1, w2, w3, Teff_jump, logMdot, dT, vinf_div_vesc, logMdot_orig
  real(dp), parameter :: Zsolar = 0.019d0   ! Vink et al. use Z = 0.019 as solar
  
  call get_star_ptr(id,s,ierr)  

  nz = s% nz
  h1 = s% net_iso(ih1)
  he4 = s% net_iso(ihe4)
  surface_h1 = s% xa(h1,1)
  surface_he4 = s% xa(he4,1)
  L1 = Lsurf   ! cgs
  M1 = Msurf   ! cgs
  T1 = Tsurf   ! cgs
  R1 = Rsurf

            ! needs to be consistent with vinf calc. in gammae subrutine !
            ! alfa = 1 for hot side, = 0 for cool side
            if (T1 > 21.d3) then   ! Note the updated bi-stability jump temperature ! 
               alfa = 1
            else if (T1 < 19.d3) then
               alfa = 0
            else ! previously used the Vink et al 2001, eqns 14 and 15 to set "jump" temperature
                 ! 1d3*(61.2d0 + 2.59d0*(-13.636d0 + 0.889d0*log10(Z/Zsolar)))
               Teff_jump = 20.d3   ! Updated value, see KPW2017
               dT = 1.d3          ! changed, see KPW2017
               if (T1 > Teff_jump + dT) then
                  alfa = 1
               else if (T1 < Teff_jump - dT) then
                  alfa = 0
               else
                  alfa = (T1 - (Teff_jump - dT)) / (2*dT)
               end if
            end if

            if (alfa > 0) then ! eval hot side wind (eqn 24)
               vinf_div_vesc = 2.6d0 ! this is the hot side galactic value
               vinf_div_vesc = vinf_div_vesc*pow(Z/Zsolar,0.13d0) ! corrected for Z
               logMdot = &
                  - 6.697d0 &
                  + 2.194d0*log10(L1/Lsun/1d5) &
                  - 1.313d0*log10(M1/Msun/30) &
                  - 1.226d0*log10(vinf_div_vesc/2d0) &
                  + 0.933d0*log10(T1/4d4) &
                  - 10.92d0*pow2(log10(T1/4d4)) &
                  + 0.85d0*log10(Z/Zsolar)             
               w1a = exp10(logMdot)               ! in Msun/yr
            else
               w1a=0
            end if
               
            if (alfa < 1) then ! eval cool side wind (eqn 25)
               vinf_div_vesc = 1.3d0 ! this is the cool side galactic value
               vinf_div_vesc = vinf_div_vesc*pow(Z/Zsolar,0.13d0) ! corrected for Z
               logMdot = &
                  - 6.688d0 &
                  + 2.210d0*log10(L1/Lsun/1d5) &
                  - 1.339d0*log10(M1/Msun/30) &
                  - 1.601d0*log10(vinf_div_vesc/2d0) &
                  + 1.07d0*log10(T1/2d4) &
                  + 0.85d0*log10(Z/Zsolar) 
                  w2a = exp10(logMdot)             ! in Msun/yr
            else
               w2a=0
            end if     
            w = alfa*w1a + (1 - alfa)*w2a    
            w_vink01 =  w  
       !    if (dbg) write(*,*) 'wind', w_vink
end subroutine Vink01

subroutine WWLR(id, Lsurf, Msurf, Rsurf, Tsurf, X, Y, Z, w, ierr)

  type (star_info), pointer :: s
  real(dp), intent(in) :: Lsurf, Msurf, Rsurf, Tsurf, X, Y, Z ! photospheric values (cgs)
  integer, intent(in) :: id
  integer, intent(out) :: ierr
  real(dp) :: L1, M1, T1, R1
! === real(dp), parameter :: alpha = 1./1.49 ! Mokiem 2007 cl !0.66d0  - ! NOW set in inlist ! ===
! force multiplier parameter representative of O stars - 
! otherwise Teff dependence needs to be included
  real(dp), parameter :: dT1 = 3.d3
! Interpolation width of the first bi-stability jump. 
! Note that a small dT results in a steep change
! in Mdot while a larger dT yields a more gradual change. 
  real(dp), parameter :: dT2 = 1.5d3
! Interpolation width of the second bi-stability jump. 
! === real(dp), parameter :: logD0_1 = 20.40d0  ! Mokiem 2007 cl - ! NOW set in inlist ! ===
! The offset of the logarithmic WLR before (hot side) the first bi-stability,
! Eq. 12 and Table 3 by KPW2017.
! The value of this offset is changed after the bi-stability regions. Units refer to cgs.
! Clumping-corrected values can be different, 
! e.g. 20.23d0 by Mokiem et al. (2007) A&A 473, 603.
  real(dp), parameter :: Teff_jump1 = 20.d3  
! FIRST bi-stability jump temperature (from observations)
  real(dp), parameter :: Teff_jump2 = 10.d3  
! SECOND bi-stability jump temperature (from observations) 
  real(dp), parameter :: deltaD0_1 = 0.35d0
! The size (=increase of log Dmom) over the first bi-stability jump, Eq. 21 by KPW2017. 
  real(dp), parameter :: deltaD0_2 = 0.d0
! The size of the second bi-stability jump, assumed to be zero here
  real(dp), intent(out) :: w
  real(dp) :: alfa1, w1, w2   
  real(dp) :: logMdot, logDmom, logD0_2, logD0_3 ! log mass-loss rate, log wind momentum,
                                                      ! and constants to increase the wind momentum over the bi-stability 

! === calculate WLR offset for after the bi-stabilities
  logD0_2 = WLR_logD0 + deltaD0_1 
! The offset of the WLR after the first bi-stability (and before the second bi-stability). 
  logD0_3 = logD0_2 + deltaD0_2 
! The offset of the WLR after the second bi-stability. 

  call get_star_ptr(id,s,ierr) 
  call gammae(id,ierr)    ! this routine should call in all relevant quantities ! 

  L1 = Lsurf   ! cgs
  M1 = Msurf   ! cgs
  T1 = Tsurf   ! cgs
  R1 = Rsurf

 if (T1 .ge. Teff_jump1 - dT1) then 
! === The WLR, Eq. 12 KPW2017 ===  
    logDmom = log10(L1/Lsun)/WLR_alpha + WLR_logD0 
! Eq. 19 KPW2017
    logMdot = logDmom - log10(vinf) - 0.5d0 * log10(R1/Rsun) + log10(secyer) - log10(Msun)
    w1 = exp10(logMdot)
    w_wlr = w1
 endif
! === Calculation of Mdot for Teff_jump1 + dT1  > T > Teff_jump2 - dT1  ===
!     corrsponding to first jump (cool solution), cool region and 2nd jump (warm solution)  
 if (T1 .le. Teff_jump1 + dT1 .and. T1 .ge. Teff_jump2 - dT2) then 
    logDmom = log10(L1/Lsun)/WLR_alpha + logD0_2 
    logMdot = logDmom - log10(vinf) - 0.5d0 *log10(R1/Rsun) + log10(secyer) - log10(Msun)  
    w2 = exp10(logMdot)
    w_wlr = w2
 endif
! --- INTERPOLATION for the FIRST bi-stability jump ---  
 if (Teff_jump1 + dT1 > T1 .and. T1 > Teff_jump1 - dT1) then
    alfa1 = (T1 - (Teff_jump1 - dT1)) / (2.d0 * dT1)
    w_wlr = alfa1 * w1 + (1.d0 - alfa1) * w2
 endif
! - after the second jump
 if (T1 .le. Teff_jump2 + dT2) then
    logDmom = log10(L1/Lsun)/WLR_alpha + logD0_3 
    logMdot = logDmom - log10(vinf) - 0.5d0 *log10(R1/Rsun) + log10(secyer) - log10(Msun)  
    w_wlr = exp10(logMdot)
 endif
    w = w_wlr
end subroutine WWLR


subroutine Sander(id, Lsurf, Msurf, Rsurf, Tsurf, X, Y, Z, w, ierr)
  type (star_info), pointer :: s
  real(dp), intent(in) :: Lsurf, Msurf, Rsurf, Tsurf, X, Y, Z ! photospheric values (cgs)
  integer, intent(in) :: id
  integer, intent(out) :: ierr
  integer :: h1, he4, nz
  real(dp) :: L1, M1, R1, T1, surface_h1, surface_he4, logMdot
  real(dp) :: alf, logLnLs, Ln, logMdot10, Mdot10
  logical, parameter :: dbg = .false.
  real(dp), intent(out) :: w
  real(dp), parameter :: Zsolar = 0.019d0   ! CHECK
  
  call get_star_ptr(id,s,ierr)  

  nz = s% nz
  h1 = s% net_iso(ih1)
  he4 = s% net_iso(ihe4)
  surface_h1 = s% xa(h1,1)
  surface_he4 = s% xa(he4,1)
  L1 = Lsurf   ! cgs
  M1 = Msurf   ! cgs
  T1 = Tsurf   ! cgs
  R1 = Rsurf
  
  alf = 0.32d0 * log10(Z/Zsolar) + 1.40d0
  logLnLs = - 0.87d0 * log10(Z/Zsolar) + 5.06d0
  Ln = Lsun * exp10(logLnLs) 
  logMdot10 = - 0.75d0 * log10(Z/Zsolar) - 4.06d0
  Mdot10 = exp10(logMdot10) ! in Msun yr^-1

  logMdot = Mdot10 * (log10(L1/Ln))**alf * (0.1*L1/Ln)**(3./4.)
 
  w_sander = exp10(logMdot)
  
  w = w_sander

  end subroutine Sander


! =====================
  !****
      integer function how_many_extra_history_columns(id)
         integer, intent(in) :: id
         integer :: ierr
         type (star_info), pointer :: s
         ierr = 0
         call star_ptr(id, s, ierr)
         if (ierr /= 0) return
         how_many_extra_history_columns = 19
      end function how_many_extra_history_columns
      
  !****
      
      integer function how_many_extra_profile_columns(id)
         integer, intent(in) :: id
         integer :: ierr
         type (star_info), pointer :: s
         ierr = 0
         call star_ptr(id, s, ierr)
         if (ierr /= 0) return
         how_many_extra_profile_columns = 0
      end function how_many_extra_profile_columns


subroutine data_for_extra_history_columns(id, n, names, vals, ierr)
         integer, intent(in) :: id, n
         character (len=maxlen_history_column_name) :: names(n)
         real(dp) :: vals(n)
         type(star_info), pointer :: s
         integer, intent(out) :: ierr
         ierr = 0
         call star_ptr(id,s,ierr)
         if(ierr/=0) return

   call gammae(id,ierr) 
   ! note: do NOT add these names to history_columns.list
   ! the history_columns.list is only for the built-in log column options.
   ! it must not include the new column names you are adding here.

   ! extra column 1
   names(1) = "Gamma_e"   !
   vals(1) = Gamma_e

   ! extra column 2
   names(2) = "vesc" ! escape velocity in cgs
   vals(2) = vesc

   ! extra column 3
   names(3) = "vinf" ! terminal wind velocity in cgs
   vals(3) = vinf

   ! extra column 4
   names(4) = "w_vink01" ! 
   vals(4) = w_vink01

   ! extra column 5
   names(5) = "use_w_vink01"     !
   vals(5) = use_w_vink01

   ! extra column 6
   names(6) = "w_vink18"     ! 
   vals(6) = w_vink18

   ! extra column 7
   names(7) = "use_w_vink18"    !
   vals(7) = use_w_vink18

   ! extra column 8
   names(8) = "w_leuven"  ! 
   vals(8) = w_leuven

  ! extra column 9
   names(9) = "use_w_leuven"
   vals(9) = use_w_leuven

  ! extra column 10
   names(10) = "w_krticka"
   vals(10) = w_krticka

  ! extra column 11
   names(11) = "use_w_krticka"  ! 
   vals(11) = use_w_krticka

  ! extra column 12
   names(12) = "w_beasor" 
   vals(12) = w_beasor

  ! extra column 13
   names(13) = "use_w_beasor"
   vals(13) = use_w_beasor

  ! extra column 14
   names(14) = "w_kee"
   vals(14) = w_kee

  ! extra column 15
   names(15) = "use_w_kee"    
   vals(15) = use_w_kee

  ! extra column 16
   names(16) = "w_sander"
   vals(16) = w_sander

  ! extra column 17
   names(17) = "use_w_sander"    
   vals(17) = use_w_sander

  ! extra column 18
   names(18) = "f_rot"         ! rotational enhancement 
   vals(18) = f_rot

  ! extra column 19
   names(19) = "Mdot_orig"     ! ! mass-loss rates before applying f_rot
   vals(19) = Mdot_orig

! If you add / remove columns, it has to be synchronized with history column number 
! at the beginning of this file. 
!
   ierr = 0
  end subroutine data_for_extra_history_columns

  subroutine data_for_extra_profile_columns(id, n, nz, names, vals, ierr)
         integer, intent(in) :: id, n, nz
         character (len=maxlen_profile_column_name) :: names(n)
         real(dp) :: vals(nz,n)
         integer, intent(out) :: ierr
         type (star_info), pointer :: s
         integer :: k
         ierr = 0
         call star_ptr(id, s, ierr)
         if (ierr /= 0) return
    !note: do NOT add the extra names to profile_columns.list
    ! the profile_columns.list is only for the built-in profile column options.
    ! it must not include the new column names you are adding here.
    ! here is an example for adding a profile column
    !if (n /= 1) stop 'data_for_extra_profile_columns'
   !   names(1) = 'extra_jdot'
   ! do k = 1, nz
   !    vals(k,1) = extra_jdot(k)  ! 
   ! end do

  end subroutine data_for_extra_profile_columns

  !****
      
  subroutine extras_after_evolve(id, ierr)
    integer, intent(in) :: id
    integer, intent(out) :: ierr
    type (star_info), pointer :: s
    ierr = 0
    call star_ptr(id, s, ierr)
    if (ierr /= 0) return
  end subroutine extras_after_evolve
  
  !****

  subroutine alloc_extra_info(s)
    integer, parameter :: extra_info_alloc = 1
    type (star_info), pointer :: s
    call move_extra_info(s,extra_info_alloc)
  end subroutine alloc_extra_info

  !****
      
  subroutine unpack_extra_info(s)
    integer, parameter :: extra_info_get = 2
    type (star_info), pointer :: s
    call move_extra_info(s,extra_info_get)
  end subroutine unpack_extra_info

  !****
      
  subroutine store_extra_info(s)
    integer, parameter :: extra_info_put = 3
    type (star_info), pointer :: s
    call move_extra_info(s,extra_info_put)
  end subroutine store_extra_info

  !****
      
  subroutine move_extra_info(s,op)
    integer, parameter :: extra_info_alloc = 1
    integer, parameter :: extra_info_get = 2
    integer, parameter :: extra_info_put = 3
    type (star_info), pointer :: s
    integer, intent(in) :: op
    
    integer :: i, j, num_ints, num_dbls, ierr
         
    i = 0
    ! call move_int or move_flg    
    num_ints = i
         
    i = 0
    ! call move_dbl       
    
    num_dbls = i

    if (op /= extra_info_alloc) return
    if (num_ints == 0 .and. num_dbls == 0) return

    ierr = 0
    call star_alloc_extras(s% id, num_ints, num_dbls, ierr)
    if (ierr /= 0) then
       write(*,*) 'failed in star_alloc_extras'
       write(*,*) 'alloc_extras num_ints', num_ints
       write(*,*) 'alloc_extras num_dbls', num_dbls
       stop 1
    end if

  contains

    subroutine move_dbl(dbl)
      real(dp) :: dbl
      i = i+1
      select case (op)
      case (extra_info_get)
         dbl = s% extra_work(i)
      case (extra_info_put)
         s% extra_work(i) = dbl
      end select
    end subroutine move_dbl

    subroutine move_int(int)
      integer :: int
      i = i+1
      select case (op)
      case (extra_info_get)
         int = s% extra_iwork(i)
      case (extra_info_put)
         s% extra_iwork(i) = int
      end select
    end subroutine move_int

    subroutine move_flg(flg)
      logical :: flg
      i = i+1
      select case (op)
      case (extra_info_get)
         flg = (s% extra_iwork(i) /= 0)
      case (extra_info_put)
         if (flg) then
            s% extra_iwork(i) = 1
         else
            s% extra_iwork(i) = 0
         end if
      end select
    end subroutine move_flg

  end subroutine move_extra_info

end module run_star_extras

