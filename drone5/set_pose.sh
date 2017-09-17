sed -i "0,/<x> .* <\/x>/s//<x> $1 <\/x>/" ekf_state_estimator_config.xml
sed -i "s#<x_0> .* </x_0>#<x_0> $1 </x_0>#g" params_localization_obs.xml
sed -i "0,/<x> .* <\/x>/s//<x> $1 <\/x>/" robot_localization.xml

sed -i "0,/<y> .* <\/y>/s//<y> $2 <\/y>/" ekf_state_estimator_config.xml
sed -i "s#<y_0> .* </y_0>#<y_0> $2 </y_0>#g" params_localization_obs.xml
sed -i "0,/<y> .* <\/y>/s//<y> $2 <\/y>/" robot_localization.xml

sed -i "0,/<z> .* <\/z>/s//<z> $3 <\/z>/" ekf_state_estimator_config.xml
sed -i "s#<z_0> .* </z_0>#<z_0> $3 </z_0>#g" params_localization_obs.xml
sed -i "0,/<z> .* <\/z>/s//<z> $3 <\/z>/" robot_localization.xml

sed -i "0,/<yaw> .* <\/yaw>/s//<yaw> $4 <\/yaw>/" ekf_state_estimator_config.xml
sed -i "s#<yaw_0> .* </yaw_0>#<yaw_0> $4 </yaw_0>#g" params_localization_obs.xml
sed -i "0,/<yaw> .* <\/yaw>/s//<yaw> $4 <\/yaw>/" robot_localization.xml
