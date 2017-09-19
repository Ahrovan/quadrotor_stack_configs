sed -i "s#<x> .* </x>#<x> $1 </x>#g" ekf_state_estimator_config.xml
sed -i "s#<x_0> .* </x_0>#<x_0> $1 </x_0>#g" params_localization_obs.xml
sed -i "s#<x> .* </x>#<x> $1 </x>#g" robot_localization.xml

sed -i "s#<y> .* </y>#<y> $2 </y>#g" ekf_state_estimator_config.xml
sed -i "s#<y_0> .* </y_0>#<y_0> $2 </y_0>#g" params_localization_obs.xml
sed -i "s#<y> .* </y>#<y> $2 </y>#g" robot_localization.xml

sed -i "s#<z> .* </z>#<z> $3 </z>#g" ekf_state_estimator_config.xml
sed -i "s#<z_0> .* </z_0>#<z_0> $3 </z_0>#g" params_localization_obs.xml
sed -i "s#<z> .* </z>#<z> $3 </z>#g" robot_localization.xml

sed -i "s#<yaw> .* </yaw>#<yaw> $4 </yaw>#g" ekf_state_estimator_config.xml
sed -i "s#<yaw_0> .* </yaw_0>#<yaw_0> $4 </yaw_0>#g" params_localization_obs.xml
sed -i "s#<yaw> .* </yaw>#<yaw> $4 </yaw>#g" robot_localization.xml
