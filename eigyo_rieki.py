{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "# pip install requests\n",
    "from kanjize import int2kanji,kanji2int\n",
    "from bs4 import BeautifulSoup\n",
    "import requests\n",
    "import re\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "def eigyo_rieki(url):\n",
    "    \n",
    "\n",
    "    r=requests.get(url)\n",
    "\n",
    "    soup=BeautifulSoup(r.text,\"html.parser\")\n",
    "    elems=soup.find_all(\"tbody\")\n",
    "    item3=[]\n",
    "    for item in elems:\n",
    "        item1=item.getText()\n",
    "        item2=re.findall(r\"\\d+億\\d+万|-\\d+億\\d+万|\\d+万|-\\d+万\",item1)\n",
    "        item3.append(item2)\n",
    "\n",
    "    items=[]\n",
    "    item3_1=item3[0]\n",
    "    for item3_1_1 in item3_1:\n",
    "        item3_1_1=item3_1_1.replace(\"億\",\"\")\n",
    "        item3_1_1=item3_1_1.replace(\"万\",\"\")\n",
    "        if item3_1_1[0]==\"0\":\n",
    "            item3_1_1=item3_1_1[2:]\n",
    "        item3_1_1=int(item3_1_1)\n",
    "        items.append(item3_1_1)\n",
    "\n",
    "    j=51\n",
    "    item_results=[]\n",
    "    while j<=101:\n",
    "        item_result=[]\n",
    "        for i in range(5):\n",
    "            if j==102:\n",
    "                break\n",
    "            item_result.append(items[j])\n",
    "            j+=1\n",
    "        item_results.append(item_result)\n",
    "\n",
    "\n",
    "    df=pd.DataFrame(item_results, index=[\"2010\",\"2011\",\"2012\",\"2013\",\"2014\",\"2015\",\"2016\",\"2017\",\"2018\",\"2019\",\"2020\"],columns=[\"1Q\",\"2Q\",\"3Q\",\"4Q\",\"通期\"])\n",
    "    print(df)\n",
    "\n",
    "    df.plot.bar()\n",
    "    return df\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "          1Q        2Q        3Q        4Q        通期\n",
      "2010   -5000   94700.0  198600.0  223300.0  511600.0\n",
      "2011   87600  119700.0    9200.0  182600.0   48100.0\n",
      "2012    3400  116800.0  -27000.0   67500.0  187700.0\n",
      "2013  -75600  146200.0  -35500.0  182800.0  217900.0\n",
      "2014   88500    9200.0  -36500.0  209300.0  351500.0\n",
      "2015   36300   82900.0  -34300.0   76400.0  161300.0\n",
      "2016   15100   79400.0   25600.0   66400.0  186500.0\n",
      "2017   74800  138800.0   45800.0  142500.0  401900.0\n",
      "2018  -17800   23300.0  -61700.0   66600.0    1400.0\n",
      "2019  104400  189200.0   -4600.0  103600.0  392600.0\n",
      "2020 -495500       NaN       NaN       NaN       NaN\n",
      "         1Q       2Q       3Q        4Q        通期\n",
      "2010  29500  42600.0  16700.0   61400.0   15200.0\n",
      "2011 -29300  31600.0   1600.0   67300.0   71200.0\n",
      "2012   8100  33100.0  -5500.0   69000.0  104700.0\n",
      "2013  23600  31800.0   8800.0   88000.0  152200.0\n",
      "2014  52300  24300.0  37200.0  104100.0  217900.0\n",
      "2015  83200  57900.0  27900.0   10100.0  269100.0\n",
      "2016  23000   2300.0   6700.0   92000.0  124000.0\n",
      "2017  35500   2700.0  47900.0  108100.0  212200.0\n",
      "2018  39400  17300.0  38100.0   89400.0  184200.0\n",
      "2019  29000   9900.0  14100.0   43300.0   96300.0\n",
      "2020 -95900      NaN      NaN       NaN       NaN\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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vxE4o454AGPqyfEA8EAd8aV15TAzayzLj87v62J7vr08r/vLmm8kNDNrom666Sb69esHQHV1Nf/6r/9K37596devH9/4xjdYsmRJpvn9NF4zsyaoqqqKd999d/f3q6++mohg4cKFFBUVsXz5cgYNGsTChQvp0aNHJm3wGYiZWROzZcsWrrzySm699VYAtm3bxuzZs5k4cSJFRUUA9OzZk8svv5xZs2Zl1g4XEDOzJmbs2LFceeWVdOqUu5thw4YNdO7cefeLpHbJ+mm8HsIysxavKb158re//S0bN27knHPO2R3r2LEja9eupbq6mpKSEl599VVOOOGEzJ/G6wJiZtaEzJ8/n/Xr13PmmWcC8MYbb3DppZcyZMgQrrrqKu644w6efvppxo8fz8qVK3nssccya4sLiJlZSoW47Pauu+7a43u/fv2YNWsW1dXV/OQnP6Fv374UFRXRvn17iouLefLJJxkyZEgmbXEBMTNrwhYsWABASUkJ48aNY9y4cbuXbd26dY8rtfLNk+hmZs1UWVkZPXvm92bHmlxAzMwsFRcQMzNLxQXEzMxScQExM7NUfBWWmVlKNW9AzIfPchNjdXU13/3ud7n//vuZN28e9957LyUlJRQVFbF06VIefvhhvv71r3P77bfTq1cvjjrqKMaPH893v/tdRo0axec+9zneeustPvjggwa312cgZmZNSElJCVdeeSXXXXcdw4YN42c/+xknnngiknjppZcYOHAg77//Pi+//DJPPvkkv/zlL3nnnXf4/e9/zw9+8AMWLFjAgAH5udveZyBmZk1M//796devH1OnTuWee+6htLSUdevWMXz4cFq1akVlZSX9+vVj2rRptG3blhNOOIFjjjmGoUOHMnXqVP7whz/kpR0+AzEza0L+9Kc/8dxzz7FixQq2b9/OqaeeyllnncWXv/xlhg0btscDFceOHcvEiRN3f//Rj35EVVUVp556al7a4jMQM7MmZOPGjbz66qssWbKE3r17c+yxx9KlSxdWrVpF3759eeSRR3av+/bbb/PRRx/t/j5nzhxWrFjB0qVL89IWFxAzsybkS1/6El27dt39tsHbbrtt9xDW66+/zvbt25kxYwZ33HEHhxxyCG3btuW9995j06ZNnH/++QwbNoxVq1blpS0NKiCSzgGGAL0jonsS6w9MB95LVnsrIkZIEnALMAAo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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "urls=[{\"name\":\"吉野家\",\"url\":\"https://irbank.net/E03153/quarter\"},{\"name\":\"松屋\",\"url\":\"https://irbank.net/E03017/quarter\"}]\n",
    "name_list=[d.get(\"name\") for d in urls]\n",
    "url_list=[d.get(\"url\") for d in urls]\n",
    "with pd.ExcelWriter(\"eigyo_rieki.xlsx\",engine=\"openpyxl\") as writer:\n",
    "    for i in range(len(url_list)):\n",
    "        df=eigyo_rieki(url_list[i])\n",
    "        df.to_excel(writer,sheet_name=name_list[i],index=False)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
