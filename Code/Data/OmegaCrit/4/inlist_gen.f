! Inlist file used by Z. Keszthelyi et al. 
! Please see run star extras for more details. 
!
&star_job
!========= Parameters in run_star_extras  ===============================================
extras_lrpar = 2
extras_rpar(1) = 0.67114d0  ! WLR alpha = 1 /x 
extras_rpar(2) = 20.40d0  ! WLR offset, logD0 

extras_lcpar = 1
! in inlist_grid 
! extras_cpar(1) = 'route1'   

!========= output profile and others ===============================================
 save_model_when_terminate = .false.
!save_model_filename = 'models/test6/MB0R0.mod'
 write_profile_when_terminate = .false.
!filename_for_profile_when_terminate = 'models/test6/last_MB0R0.data'
 pgstar_flag = .false.
 pause_before_terminate = .false. 

 set_initial_age = .true.
 initial_age = 0 ! in years
 set_initial_model_number = .true.
 initial_model_number = 0

!========= new METALLICITY ===============================================
  relax_initial_Z = .true.      
  ! gradually changes abundances
  new_Z = 14.d-3  
  relax_initial_Y = .true.
  new_Y = 0.266d0  
  set_uniform_initial_composition = .true.
  initial_h1 = 0.7200d0    !!! MW: 0.720d0  
  initial_he4 = 0.266d0   !!! MW: 0.266d0  
  initial_h2 = 0.0
  initial_he3 = 0.0   
  initial_zfracs = 8   ! 8 = Przybilla,  6 = Asplund 2009, 5 = Asplund 2005, 0 = custom
!============ initial surface rotation ===================================  
 change_v_flag = .true.
 new_v_flag = .true. 
 change_rotation_flag = .true.
 new_rotation_flag = .true.
 set_omega_div_omega_crit_step_limit = 50
! set_initial_omega_div_omega_crit = .true.
 change_D_omega_flag = .true.
 new_D_omega_flag = .true.
 new_omega_div_omega_crit = 0.6 
 set_omega_div_omega_crit = .true.
! near_zams_relax_omega_div_omega_crit = .true.
! relax_omega_div_omega_crit = .true.
! relax_omega_max_yrs_dt = 1.0d0    ! keep timesteps small to prevent significant evolution
! === note that "input" rotation is not equal to what we call "ZAMS" rotation === !
! new_surface_rotation_v = 440  ! in km/s  
! set_surf_rotation_v_step_limit = 50
! set_surface_rotation_v = .true.  !
! near_zams_relax_initial_surface_rotation_v = .true.
! set_initial_surface_rotation_v = .true.  ! 

 num_steps_to_relax_rotation = 50
 num_steps_to_relax_composition = 50

/  !end of star_job namelist

&controls   
!========= The OUTPUT =============================  
!         - filename - 
 star_history_name = 'out.data' 
!--------  initial stellar MASS ------------
! initial_mass = 18  ! in inlist_grid! 
!================================
 am_D_mix_factor = 0.0333      ! mixing efficiency (f_c in literature)
 am_gradmu_factor = 0.1      ! f_mu
!======= MASS-LOSS RATES ============================= 
 mdot_omega_power = 0.0    !0.43  ! We use an alternative formalism in the run_star_extras.
                           ! (The two should not be applied together.) 
!=============== Routes + rot.enhancement     
 use_other_wind =  .true.           ! ON
!=============================================
max_mdot_redo_cnt = 10
min_years_dt_for_redo_mdot = 0
surf_w_div_w_crit_limit = 0.95d0  ! def: 0.99d0 
surf_w_div_w_crit_tol = 0.05d0
mdot_revise_factor = 1.1d0
implicit_mdot_boost = 0.1d0

! solver settings

! === solver settings ===
 use_gold_tolerances = .false.
! gold_tol_residual_norm1 = 1d-11
! gold_tol_max_residual1 = 1d-9
! gold_iter_for_resid_tol2 = 5
! gold_tol_residual_norm2 = 1d-8
! gold_tol_max_residual2 = 1d-6
! gold_iter_for_resid_tol3 = 10
! gold_tol_residual_norm3 = 1d-6
! gold_tol_max_residual3 = 1d-4
! tol_bad_max_correction = 0d0
 use_gold2_tolerances = .false.  !"level 2"

  use_dedt_form_of_energy_eqn = .true.  ! better or not? if NOT: dL/dm
  convergence_ignore_equL_residuals = .true. !!! good? 
  ignore_too_large_correction = .true.
  make_gradr_sticky_in_solver_iters = .true.
  use_d_eos_dxa = .true.  ! check? 
  op_split_burn = .false. !! .true. ! needed?
!  op_split_burn_min_T = 1d9
!  op_split_burn_eps = 1d-7
!  op_split_burn_odescal = 1d-8

  do_solver_damping_for_neg_xa = .true.
  xa_scale = 1d-5
  solver_itermin = 3
! scale_max_correction = 0.1d0
!::  ignore_species_in_max_correction = .true.
  include_composition_in_eps_grav = .true.
  retry_limit = 35
  max_tries_for_retry = 35  
 ! velocity_logT_lower_bound = 8
 ! max_dt_yrs_for_velocity_logT_lower_bound = 0.1
  tol_correction_norm = 3d-5
  tol_max_correction = 3d-3
  tol_residual_norm1 = 1d-10
  tol_max_residual1 = 1d-9
  iter_for_resid_tol2 = 6

  solver_max_tries_before_reject = 35
  solver_iters_timestep_limit = 6 ! If solver uses more iterations than this, reduce the next timestep
  ignore_species_in_max_correction = .true.
  dX_mix_dist_limit = 1d-4  !

  stop_for_bad_nums = .true.  ! debug

! ===time step ===
  varcontrol_target = 1.d-4   ! default: 1.d-4
  time_delta_coeff = 1.0d0
   
  max_timestep_factor = 1.2d0
  min_timestep_factor = 0.8d0
  min_timestep_limit = 1.d-10
  timestep_factor_for_retries = 0.4d0     
  max_years_for_timestep = 1.d5       !!! keep an eye on this !!!  

  report_why_dt_limits = .true. 
  report_ierr = .true. 
  report_solver_progress = .true.
  report_solver_dt_info = .true.

  ! ===mesh parameters===
  max_allowed_nz = 20000
  mesh_delta_coeff = 1.0d0 
  okay_to_remesh = .true.
  min_dq_for_xa = 1d-4      ! avoid over-resolving composition changes
  max_dq = 0.0005           ! minimum number of cells = 1/max_dq

  max_logT_for_k_below_const_q = 100
  max_q_for_k_below_const_q = 0.99
  min_q_for_k_below_const_q = 0.99
  max_logT_for_k_const_mass = 100
  max_q_for_k_const_mass = 0.98
  min_q_for_k_const_mass = 0.98

  ! mlt++
   okay_to_reduce_gradT_excess = .true.
   gradT_excess_age_fraction = 0.95
   gradT_excess_max_change = 0.001

  ! these are to properly resolve core hydrogen and helium depletion
      delta_lg_XH_cntr_limit = 0.02d0
      delta_lg_XH_cntr_max = 0.0d0
      delta_lg_XH_cntr_min = -6.0d0
      delta_lg_XH_cntr_hard_limit = 0.03d0

      delta_lg_XHe_cntr_limit = 0.01d0
      delta_lg_XHe_cntr_max   = 0.0d0
      delta_lg_XHe_cntr_min   = -4.0d0
      delta_lg_XHe_cntr_hard_limit = 0.02d0

  ! avoid large jumps in the HR diagram
  delta_HR_limit = 0.005d0   !!! 0.005d0

!  min_T_for_acceleration_limited_conv_velocity = 1.0e0
!  max_T_for_acceleration_limited_conv_velocity = 99e9
!  mlt_accel_g_theta = 1.d-2

  dH_decreases_only = .false.
  dH_div_H_limit_min_H = 1d-4 !!! 1d-3 -6
  dH_div_H_limit = 0.9d0
  dH_div_H_hard_limit = 1d99
!  dHe_div_He_limit = -1
!  delta_lgL_He_limit = 0.1  
  delta_dX_div_X_cntr_min = -4

  dX_nuc_drop_max_A_limit = 52
  dX_nuc_drop_min_X_limit = 1d-4
  dX_nuc_drop_hard_limit = 1d99

  delta_lgL_nuc_limit = 0.01d0
  delta_lgL_nuc_hard_limit = 0.02d0
  delta_lgL_nuc_at_high_T_limit = -1
  delta_lgL_nuc_at_high_T_hard_limit = -1
  delta_lgL_nuc_at_high_T_limit_lgT_min = -1     
  max_lgT_for_lgL_nuc_limit = 9.5d0
  lgL_nuc_burn_min = 0.5d0
  lgL_nuc_drop_factor = 10

  delta_lgTeff_limit = 0.05d0   !0.03 
  delta_lgL_limit = 0.5
  delta_lgT_limit = 0.05d0
  delta_lgT_max_limit_only_after_near_zams = .true.
  delta_lgT_max_limit = 0.001     
  delta_lgT_max_hard_limit = 0.01
  delta_lgRho_cntr_limit = 0.05    ! 0.02 ! 0.005   ! default 0.05
  delta_lgRho_limit = 1.0          !0.2        ! default 1.0

!======= stopping options =========================

! xa_central_lower_limit_species(1) = 'h1' (init = 0.72 ---> )
! xa_central_lower_limit(1) = 1d-5
! xa_central_lower_limit_species(1) = 'he4'
! xa_central_lower_limit(1) = 1d-5
 
 fe_core_infall_limit = 3d7

!======== ROTATIONAL INSTABILITIES  =============================
!  set_uniform_am_nu_non_rot = .false. 
! uniform_am_nu_non_rot = 1.d14
 skip_rotation_in_convection_zones = .true.   ! do not apply rot mix in conv.         
!================================
 am_nu_factor = 1.d0
!
 use_brunt_gradmuX_form = .false. ! check if needed
!-----------------------------------------------
! factor for rot.instabilities ---» D_mix = diffusion coefficient  --» this is multiplied by f_c
!  D_mix = D_mix_nonrot + am_D_mix_factor * ( D_SI + ...)         this is f_c from Heger et al 
!===== CHEMICAL MIXING ======================================================					        
   D_DSI_factor = 1   ! dynamical shear instability
   D_SH_factor = 0    ! Solberg-Hoiland
   D_SSI_factor = 1      ! secular shear instability
   D_ES_factor = 1       ! Eddington-Sweet circulation
   D_GSF_factor = 1      ! Goldreich-Schubert-Fricke
   D_ST_factor = 0  ! Spruit-Tayler dynamo 

!====== ANGULAR MOMENTUM ============================================== 
   am_nu_DSI_factor = 1 ! this is for ang.mom. transport
   am_nu_SH_factor = 0
   am_nu_SSI_factor = 1
   am_nu_ES_factor = 1
   am_nu_GSF_factor = 1
   am_nu_ST_factor = 0     ! dynamo turned OFF
     
!=============== MIXING LENGTH PARAMETERS ========================

  mixing_length_alpha = 1.8d0       
  use_ledoux_criterion = .true.
 !::: alpha_semiconvection = 1.d0

! ============= OVERSHOOTING ====================================
!------------- exponential decay --------------------- 
! f0 is at the expense of the core, inward
! f is the exponential parameter
! it is very roughly true that 10 * (f - f0) = alpha_ov 
  overshoot_scheme(1) = 'exponential'
  overshoot_zone_type(1) = 'burn_H'  
  overshoot_zone_loc(1) = 'core'
  overshoot_bdy_loc(1) = 'top'
  overshoot_f(1) = 0.015
  overshoot_f0(1) = 0.005

  overshoot_scheme(2) = 'exponential'
  overshoot_zone_type(2) = 'burn_He'  
  overshoot_zone_loc(2) = 'core'
  overshoot_bdy_loc(2) = 'top'
  overshoot_f(2) = 0.015
  overshoot_f0(2) = 0.005

  overshoot_scheme(3) = 'exponential'
  overshoot_zone_type(3) = 'nonburn'
  overshoot_zone_loc(3) = 'shell'
  overshoot_bdy_loc(3) = 'any'
  overshoot_f(3) = 0.0010
  overshoot_f0(3) = 0.0005

  min_overshoot_q = 0   ! 1.d-1
  overshoot_D_min = 1.d2 

!-----------------------------------------------------------------------------
! profile 
 write_profiles_flag = .false. 
 profile_interval = 190000
 profile_data_prefix = '../models/test6/prof.'
 profile_data_suffix = '.data'
 max_num_profile_models = 10
 profiles_index_name = 'profiles.index'
 photo_directory = 'photos'
 photo_interval = 190000
 terminal_interval = 190000
 do_history_file = .true.     
 max_model_number = 190000    
 history_interval = 1     

/ ! end of controls namelist

&eos
/ ! end of eos namelist

&kap
      kap_file_prefix = 'a09'    ! 'gs98' 'a09'  'OP_a09' 'OP_gs98'
      kap_CO_prefix   = 'a09_co' ! 'gs98_co' 'a09_co'
      kap_lowT_prefix = 'lowT_fa05_a09p'
      use_Type2_opacities = .true.
      Zbase = 0.014
/ ! end of kap namelist

