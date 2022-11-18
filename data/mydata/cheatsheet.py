python ./generate.py -o "../data/outputs/v1/myoptions.json" -s "../data/clean/032_Agreement_1_x_1_0.bvh" -a "../data/mydata/WelcomeTCKO.wav"
python ./generate.py -o "../data/outputs/v1/myoptions.json" -s "../data/clean/035_Disagreement_2_x_1_0.bvh" -a "../data/mydata/WelcomeTCKO.wav"


rewrite data_pipleline.py so it loads the clean Files
add option to datapipleline coft so you can reuse the truncated files
remove code in : 288-461
then keep:
            # Extracting Audio Features #
then resume

consider setting in info.csv
033_Agreement_2.wav	09:14:08:07   	09:16:00:13   	00:01:52:05   		20210826_002_Agreement_3_01.fbx	09:14:05:47	09:15:57:56	00:01:59:09	09:14:11:50	Agreement	2	09:14:17:21	09:15:56:07	033_Agreement_2.bvh	TRUE									
VALIDATION to FALSE!!!!

Agreement0 stalls at 1.0 (0.99 ok)
Agreement1 stalls at 0.99 (0.95 ok)
Agreement2 stalls already at 0.9