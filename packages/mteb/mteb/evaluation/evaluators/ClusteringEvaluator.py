import logging

import numpy as np
import sklearn
import sklearn.cluster
import time

logger = logging.getLogger(__name__)

from .Evaluator import Evaluator


class ClusteringEvaluator(Evaluator):
    def __init__(self, sentences, labels, clustering_batch_size=500, batch_size=32, limit=None, **kwargs):
        super().__init__(**kwargs)
        if limit is not None:
            sentences = sentences[:limit]
            labels = labels[:limit]
        self.sentences = sentences
        self.labels = labels
        self.clustering_batch_size = clustering_batch_size
        self.batch_size = batch_size

    def __call__(self, model):
        logger.info(f"Encoding {len(self.sentences)} sentences...")
        print(time.time())

        corpus_embeddings = np.asarray(model.encode(self.sentences, batch_size=self.batch_size))
        print(time.time())

        logger.info("Fitting Mini-Batch K-Means model...")

        print(time.time())
        clustering_model = sklearn.cluster.MiniBatchKMeans(
            n_clusters=len(set(self.labels)), batch_size=self.clustering_batch_size, n_init="auto"
        )
        clustering_model.fit(corpus_embeddings)
        print(time.time())

        cluster_assignment = clustering_model.labels_

        logger.info("Evaluating...")
        v_measure = sklearn.metrics.cluster.v_measure_score(self.labels, cluster_assignment)
        print(time.time())

        return {"v_measure": v_measure}
