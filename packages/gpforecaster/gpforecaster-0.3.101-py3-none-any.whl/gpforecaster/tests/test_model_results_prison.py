import pickle
import unittest

import tsaugmentation as tsag

from gpforecaster.model.gpf import GPF


class TestModel(unittest.TestCase):
    def setUp(self):
        self.data = tsag.preprocessing.PreprocessDatasets(
            "prison", freq="Q"
        ).apply_preprocess()
        self.n = self.data["predict"]["n"]
        self.s = self.data["train"]["s"]
        self.res_type = "fitpred"
        self.res_measure = "mean"
        self.input_dir = "./results/gpf/"
        self.gpf = GPF("tourism", self.data, input_dir=self.input_dir)

    def test_correct_train(self):
        model, like = self.gpf.train(epochs=10)
        self.assertIsNotNone(model)

    def test_predict_shape(self):
        model, like = self.gpf.train(epochs=10)
        preds, preds_scaled = self.gpf.predict(model, like)
        self.assertTrue(preds[0].shape == (self.n, self.s))

    def test_results_interval(self):
        model, like = self.gpf.train(epochs=100)
        preds, preds_scaled = self.gpf.predict(model, like)
        res = self.gpf.metrics(preds[0], preds[1])
        self.assertLess(res["mase"]["bottom"], 40)

    def test_wall_time(self):
        model, like = self.gpf.train(epochs=10)
        preds, preds_scaled = self.gpf.predict(model, like)
        res = self.gpf.metrics(preds[0], preds[1])
        self.assertLess(res["wall_time"]["wall_time_total"], 100)

    def test_output_results(self):
        model, like = self.gpf.train(epochs=10)
        preds, preds_scaled = self.gpf.predict(model, like)
        res = self.gpf.metrics(preds[0], preds[1])
        self.gpf.store_results(
            res, res_type=self.res_type, res_measure=self.res_measure
        )
        with open(
            f"{self.gpf.input_dir}results_{self.res_type}_{self.res_measure}_gp_{self.gpf.gp_type}_cov_{self.gpf.dataset}_{self.gpf.model_version}.pickle",
            "rb",
        ) as handle:
            output_res = pickle.load(file=handle)
        self.assertIsNotNone(output_res["mase"]["bottom"])

    def test_plot_loss_xvalidation(self):
        model, like = self.gpf.train(epochs=10)
        self.gpf.plot_losses()

    def test_plot_loss(self):
        model, like = self.gpf.train(epochs=10, cross_validation=False)
        self.gpf.plot_losses()

    def test_no_validation(self):
        model, like = self.gpf.train(
            epochs=10, cross_validation=False, no_validation=True
        )
        self.gpf.plot_losses()
