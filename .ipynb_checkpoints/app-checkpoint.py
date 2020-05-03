{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from flask import Flask, jsonify, request\n",
    "import pickle\n",
    "\n",
    "# load model\n",
    "model = pickle.load(open('model.pkl','rb'))\n",
    "\n",
    "# app\n",
    "app = Flask(__name__)\n",
    "\n",
    "# routes\n",
    "@app.route('/', methods=['POST'])\n",
    "\n",
    "def predict():\n",
    "    # get data\n",
    "    data = request.get_json(force=True)\n",
    "\n",
    "    # convert data into dataframe\n",
    "    data.update((x, [y]) for x, y in data.items())\n",
    "    data_df = pd.DataFrame.from_dict(data)\n",
    "\n",
    "    # predictions\n",
    "    result = model.predict(data_df)\n",
    "\n",
    "    # send back to browser\n",
    "    output = {'results': int(result[0])}\n",
    "\n",
    "    # return data\n",
    "    return jsonify(results=output)\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(port = 5000, debug=True)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "mongodb-playgrounds",
   "language": "python",
   "name": "mongodb-playgrounds"
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
   "version": "3.7.4"
  },
  "varInspector": {
   "cols": {
    "lenName": 16,
    "lenType": 16,
    "lenVar": 40
   },
   "kernels_config": {
    "python": {
     "delete_cmd_postfix": "",
     "delete_cmd_prefix": "del ",
     "library": "var_list.py",
     "varRefreshCmd": "print(var_dic_list())"
    },
    "r": {
     "delete_cmd_postfix": ") ",
     "delete_cmd_prefix": "rm(",
     "library": "var_list.r",
     "varRefreshCmd": "cat(var_dic_list()) "
    }
   },
   "types_to_exclude": [
    "module",
    "function",
    "builtin_function_or_method",
    "instance",
    "_Feature"
   ],
   "window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
