import json
from copy import deepcopy

from kubernetes import client

from .enums import SecretType, ServiceType, IngressRulePathType, PVCAccessMode, VolumeModes, UpdateStrategy, \
    PodManagementPolicy
from .templates import PodSpec, PodTemplateSpec, JobTemplateSpec, Container, V1Primitive, ObjectMetadata, \
    LabelSelector, dict_str


class Job(PodTemplateSpec, ObjectMetadata):
    def __init__(self, name: str, c: Container):
        super().__init__(c)
        ObjectMetadata.__init__(self, name)

        self._job = client.V1Job(
            api_version="batch/v1",
            kind="Job",
            spec=client.V1JobSpec(
                template=client.V1PodTemplateSpec()
            )
        )

    @property
    def manifest(self) -> client.V1Job:
        o = deepcopy(self._job)
        o.metadata = self._metadata
        o.spec.template = super().manifest
        return o

    def set_backoff_limit(self, n: int):
        self._job.spec.backoff_limit = n

    def set_ttl_seconds_after_finished(self, n: int):
        self._job.ttl_seconds_after_finished = n

    def set_parallelism(self, n: int):
        self._job.parallelism = n


class CronJob(JobTemplateSpec, ObjectMetadata):
    def __init__(self, name: str, c: Container):
        super().__init__(c)
        ObjectMetadata.__init__(self, name)

        self._cj = client.V1CronJob(
            api_version='batch/v1',
            kind='CronJob',
            metadata=client.V1ObjectMeta(name=name),
            spec=client.V1CronJobSpec(
                job_template=client.V1JobTemplateSpec(),
                schedule='0 0 * * *'
            )
        )

    @property
    def manifest(self) -> client.V1CronJob:
        o = deepcopy(self._cj)
        o.spec.job_template = super().manifest
        return o

    def set_annotations(self, **kwargs):
        self._cj.metadata.annotations = dict_str(**kwargs)

    def set_labels(self, **kwargs):
        self._cj.metadata.labels = dict_str(**kwargs)

    def set_pod_annotations(self, **kwargs):
        super().set_annotations(**kwargs)

    def set_pod_labels(self, **kwargs):
        super().set_labels(**kwargs)

    def set_schedule(self, cron: str):
        self._cj.spec.schedule = cron

    def set_starting_deadline_seconds(self, n: int):
        self._cj.spec.starting_deadline_seconds = n

    def set_concurrency_policy(self, policy: str):
        self._cj.spec.concurrency_policy = policy

    def set_failed_jobs_history_limit(self, n: int):
        self._cj.spec.failed_jobs_history_limit = n

    def set_successful_jobs_history_limit(self, n: int):
        self._cj.spec.successful_jobs_history_limit = n

    def set_time_zone(self, tz: str):
        self._cj.spec.time_zone = tz

    def set_suspend(self, b: bool):
        self._cj.spec.suspend = b


class Pod(PodSpec, ObjectMetadata):
    def __init__(self, name: str, c: Container):
        super().__init__(c)
        ObjectMetadata.__init__(self, name)

        self._pod = client.V1Pod(
            api_version='v1',
            kind='Pod',
        )

    @property
    def manifest(self) -> client.V1Pod:
        o = deepcopy(self._pod)
        o.metadata = self._metadata
        o.spec = super().manifest
        return o

    def set_annotations(self, **kwargs):
        self._pod.metadata.annotations = dict_str(**kwargs)

    def set_labels(self, **kwargs):
        self._pod.metadata.labels = dict_str(**kwargs)


class Deployment(PodTemplateSpec, ObjectMetadata, LabelSelector):
    def __init__(self, name: str, c: Container):
        super().__init__(c)
        ObjectMetadata.__init__(self, name)

        self._deploy = client.V1Deployment(
            spec=client.V1DeploymentSpec(
                template=client.V1PodTemplateSpec()
            )
        )

    @property
    def manifest(self) -> client.V1Deployment:
        o = deepcopy(self._deploy)
        o.metadata = self._metadata
        o.spec.selector = self._selector
        o.spec.template = super().manifest
        return o

    @property
    def selector_match_labels(self) -> dict[str, str]:
        return self._deploy.spec.selector.match_labels.copy()

    def set_annotations(self, **kwargs):
        self._deploy.metadata.annotations = dict_str(**kwargs)

    def set_labels(self, **kwargs):
        self._deploy.metadata.labels = dict_str(**kwargs)

    def set_pod_annotations(self, **kwargs):
        super().set_pod_annotations(**kwargs)

    def set_pod_labels(self, **kwargs):
        super().set_pod_labels(**kwargs)

    def set_replicas(self, n: int):
        self._deploy.spec.replicas = n

    def set_revision_history_limit(self, n: int):
        self._deploy.spec.revision_history_limit = n

    def set_strategy(self, typ: UpdateStrategy, max_surge=None, max_unavailable=None):
        self._deploy.spec.strategy = client.V1DeploymentStrategy(
            type=typ.value,
            rolling_update=client.V1RollingUpdateDeployment(max_surge=max_surge, max_unavailable=max_unavailable))


class StatefulSet(PodTemplateSpec, ObjectMetadata, LabelSelector):
    def __init__(self, name: str, c: Container):
        super().__init__(c)
        ObjectMetadata.__init__(self, name)

        self._sts = client.V1StatefulSet(
            api_version='v1',
            kind='StatefulSet',
            spec=client.V1StatefulSetSpec(
                service_name='',
                template=client.V1PodTemplateSpec()
            )
        )

    @property
    def manifest(self) -> client.V1StatefulSet:
        o = deepcopy(self._sts)
        o.metadata = self._metadata
        o.spec.selector = self._selector
        o.spec.template = super().manifest
        return o

    def set_annotations(self, **kwargs):
        self._sts.metadata.annotations = dict_str(**kwargs)

    def set_labels(self, **kwargs):
        self._sts.metadata.labels = dict_str(**kwargs)

    def set_pod_annotations(self, **kwargs):
        super().set_annotations(**kwargs)

    def set_pod_labels(self, **kwargs):
        super().set_labels(**kwargs)

    def set_replicas(self, n: int):
        self._sts.spec.replicas = n

    def set_revision_history_limit(self, n: int):
        self._sts.spec.revision_history_limit = n

    def set_strategy(self, typ: str, max_unavailable=None, partition: int = None):

        self._sts.spec.update_strategy = client.V1StatefulSetUpdateStrategy(
            type=typ,
            rolling_update=client.V1RollingUpdateStatefulSetStrategy(
                max_unavailable=max_unavailable, partition=partition))

    def set_service_name(self, name: str):
        self._sts.spec.service_name = name

    def set_persistent_volume_claim_retention_policy(self, when_deleted: str, when_scaled: str):
        o = client.V1StatefulSetPersistentVolumeClaimRetentionPolicy(when_deleted=when_deleted, when_scaled=when_scaled)
        self._sts.spec.persistent_volume_claim_retention_policy = o

    def set_pod_management_policy(self, policy: PodManagementPolicy):
        self._sts.spec.pod_management_policy = policy.value

    def add_volume_claim_templates(self, pvc: client.V1PersistentVolumeClaim):
        if self._sts.spec.volume_claim_templates:
            for p in self._sts.spec.volume_claim_templates:
                if p.metadata.name == pvc.metadata.name:
                    return
        else:
            self._sts.spec.volume_claim_templates = []

        self._sts.spec.volume_claim_templates.append(pvc)


class Secret(ObjectMetadata, V1Primitive):
    def __init__(self, name: str, typ: SecretType):
        super().__init__(name)
        V1Primitive.__init__(self)

        self._secret = client.V1Secret(
            api_version="v1",
            kind="Secret",
            type=typ.value
        )

    @property
    def manifest(self):
        sec = deepcopy(self._secret)
        sec.metadata = self._metadata
        sec.immutable = self._immutable
        if self._string_data:
            sec.string_data = self._string_data
        if self._binary_data:
            sec.data = self._binary_data

        return sec


class SecretImagePull(Secret):
    def __init__(self, name: str):
        super().__init__(name, SecretType.DockerConfigJSON)

        self._registries = {}

    def add_registry(self, registry: str, username: str, password: str, email: str):
        if self._registries.get(registry):
            return

        self._registries[registry] = {
            "username": username,
            "password": password,
            "email": email,
            "auth": self.to_base64(f"{username}:{password}")
        }

    @property
    def manifest(self):
        auth = json.dumps({"auths": self._registries})
        self.set(".dockerconfigjson", auth)

        return super().manifest


class SecretTLS(Secret):
    def __init__(self, name: str):
        super().__init__(name, SecretType.TLS)

    def set(self, tls_cert: str, tls_key: str, ca_crt: str = None):
        if ca_crt:
            super().set('ca.crt', ca_crt)

        super().set('tls.crt', tls_cert)
        super().set('tls.key', tls_key)


class SecretServiceAccountToken(Secret):
    def __init__(self, name: str):
        super().__init__(name, SecretType.ServiceAccountToken)

    def set(self, namespace: str, token: str, ca_crt: str = None):
        if ca_crt:
            super().set('ca.crt', ca_crt)

        super().set('namespace', namespace)
        super().set('token', token)


class ConfigMap(ObjectMetadata, V1Primitive):
    def __init__(self, name: str):
        super().__init__(name)
        V1Primitive.__init__(self)

        self._cm = client.V1ConfigMap(
            api_version="v1",
            kind="ConfigMap",
        )

    @property
    def manifest(self):
        cm = deepcopy(self._cm)
        cm.metadata = self._metadata
        cm.immutable = self._immutable
        if self._string_data:
            cm.data = self._string_data
        if self._binary_data:
            cm.binary_data = self._binary_data

        return cm


class Service(ObjectMetadata):
    def __init__(self, name: str):
        super().__init__(name)

        self._svc = client.V1Service(
            api_version="v1",
            kind="Service",
            spec=client.V1ServiceSpec()
        )

    @property
    def manifest(self) -> client.V1Service:
        svc = deepcopy(self._svc)
        svc.metadata = self._metadata
        return svc

    def set_selector(self, **kwargs):
        self._svc.spec.selector = dict_str(**kwargs)

    def set_type(self, t: ServiceType):
        self._svc.spec.type = t.value

    def add_port(self, name: str, port: int, target_port_or_name,
                 proto: str = None, node_port: int = None, app_protocol: str = None):
        if self._svc.spec.ports:
            for p in self._svc.spec.ports:
                if p.name == name:
                    return
        else:
            self._svc.spec.ports = []

        self._svc.spec.ports.append(client.V1ServicePort(name=name, port=port, target_port=target_port_or_name,
                                                         protocol=proto, node_port=node_port,
                                                         app_protocol=app_protocol))


class Ingress(ObjectMetadata):
    def __init__(self, name: str):
        super().__init__(name)

        self._ing = client.V1Ingress(
            api_version='networking.k8s.io/v1',
            kind='Ingress',
            spec=client.V1IngressSpec()
        )

    @property
    def manifest(self) -> client.V1Ingress:
        ing = deepcopy(self._ing)
        ing.metadata = self._metadata
        return ing

    def set_default_backend(self, service_name: str = None, service_port: int | str = None,
                            ref: client.V1TypedLocalObjectReference = None):
        self._ing.spec.default_backend = self._ingress_backend(service_name, service_port, ref)

    def set_ingress_class_name(self, name: str):
        self._ing.spec.ingress_class_name = name

    def add_rule(self, host: str, path: str, path_type: IngressRulePathType, service_name: str = None,
                 service_port: int = None, ref: client.V1TypedLocalObjectReference = None):
        backend_path = client.V1HTTPIngressPath(
            backend=self._ingress_backend(service_name, service_port, ref),
            path=path,
            path_type=path_type.value
        )

        if self._ing.spec.rules is None:
            self._ing.spec.rules = []

        for i, rule in enumerate(self._ing.spec.rules):
            if rule.host == host:
                for p in rule.http.paths:
                    if p.path == path:
                        return

                rule.http.paths.append(backend_path)

                self._ing.spec.rules[i] = rule
                return

        self._ing.spec.rules.append(
            client.V1IngressRule(
                host=host,
                http=client.V1HTTPIngressRuleValue(
                    paths=[backend_path])))

    def add_tls(self, *hosts: str, secret_name: str = None):
        if self._ing.spec.tls:
            for tls in self._ing.spec.tls:
                if secret_name == tls.secret_name:
                    return
        else:
            self._ing.spec.tls = []

        self._ing.spec.tls.append(client.V1IngressTLS(hosts=hosts, secret_name=secret_name))

    def _ingress_backend(self, service_name: str = None, service_port: int | str = None,
                         ref: client.V1TypedLocalObjectReference = None) -> client.V1IngressBackend:
        backend = client.V1IngressBackend()
        if ref:
            backend.resource = ref
            return backend

        if isinstance(service_port, int):
            port_def = client.V1ServiceBackendPort(number=service_port)
        else:
            port_def = client.V1ServiceBackendPort(name=service_port)

        backend.service = client.V1IngressServiceBackend(name=service_name, port=port_def)

        return backend


class Namespace(ObjectMetadata):
    def __init__(self, name: str):
        super().__init__(name)

        self._ns = client.V1Namespace(
            api_version='v1',
            kind='Namespace'
        )

    @property
    def manifest(self) -> client.V1Namespace:
        ns = deepcopy(self._ns)
        ns.metadata = self._metadata
        return ns


class PersistentVolumeClaim(ObjectMetadata, LabelSelector):
    def __init__(self, name: str):
        super().__init__(name)

        self._pvc = client.V1PersistentVolumeClaim(
            api_version='v1',
            kind='PersistentVolumeClaim',
            spec=client.V1PersistentVolumeClaimSpec(
                access_modes=[],
                resources=client.V1ResourceRequirements(),
            )
        )

    @property
    def manifest(self) -> client.V1PersistentVolumeClaim:
        pvc = deepcopy(self._pvc)
        pvc.metadata = self._metadata
        pvc.spec.selector = self._selector
        return pvc

    def set_access_modes(self, *args: PVCAccessMode):
        self._pvc.spec.access_modes = [a.value for a in args]

    def set_data_source(self, name: str, api_group: str, kind: str):
        self._pvc.spec.data_source = client.V1TypedLocalObjectReference(
            api_group, kind, name
        )

    def set_data_source_ref(self, name: str, namespace: str, api_group: str, kind: str):
        self._pvc.spec.data_source_ref = client.V1TypedObjectReference(
            api_group, kind, name, namespace
        )

    def set_storage_class_name(self, name: str):
        self._pvc.spec.storage_class_name = name

    def set_volume_mode(self, mode: VolumeModes):
        self._pvc.spec.volume_mode = mode.value

    def set_volume_name(self, name: str):
        self._pvc.spec.volume_name = name

    def set_resources_requests(self, size: str):
        self._pvc.spec.resources.requests = {'storage': size}

    def set_resources_limits(self, size: str):
        self._pvc.spec.resources.limits = {'storage': size}


class ServiceAccount(ObjectMetadata):
    def __init__(self, name):
        super().__init__(name)

        self._sa = client.V1ServiceAccount(
            api_version='v1',
            kind='ServiceAccount'
        )

    @property
    def manifest(self) -> client.V1ServiceAccount:
        sa = deepcopy(self._sa)
        sa.metadata = self._metadata
        return sa

    def set_automount_service_account_token(self, b: bool):
        self._sa.automount_service_account_token = b

    def add_image_pull_secrets(self, name: str):
        self._sa.image_pull_secrets.append(
            client.V1LocalObjectReference(name=name))

    def add_secret(self, ref: client.V1ObjectReference):
        self._sa.secrets.append(ref)

    def add_secret_name(self, name: str):
        self._sa.secrets.append(
            client.V1ObjectReference(name=name))


class _Role(ObjectMetadata):
    def __init__(self, name: str, kind: str):
        super().__init__(name)

        obj = client.V1Role
        if kind == 'ClusterRole':
            obj = client.V1ClusterRole

        self._role = obj(
            api_version='rbac.authorization.k8s.io/v1',
            kind=kind,
            rules=[]
        )

    @property
    def manifest(self) -> client.V1Role:
        role = deepcopy(self._role)
        role.metadata = self._metadata
        return role

    def add_rule(self, rule: client.V1PolicyRule):
        self._role.rules.append(rule)


class _RoleBinding(ObjectMetadata):
    def __init__(self, name: str, kind: str):
        super().__init__(name)

        default_role_ref_kind = 'Role'
        obj = client.V1RoleBinding
        if kind == 'ClusterRoleBinding':
            default_role_ref_kind = 'ClusterRole'
            obj = client.V1ClusterRoleBinding

        self._role_binding = obj(
            api_version='rbac.authorization.k8s.io/v1',
            kind=kind,
            role_ref=client.V1RoleRef('rbac.authorization.k8s.io', default_role_ref_kind, ''),
            subjects=[]
        )

    @property
    def manifest(self):
        rb = deepcopy(self._role_binding)
        rb.metadata = self._metadata
        return rb

    def set_role_ref(self, name: str, api_group: str = None, kind: str = None):
        self._role_binding.role_ref.name = name
        if api_group:
            self._role_binding.role_ref.api_group = api_group
        if kind:
            self._role_binding.role_ref.kind = kind

    def add_subject(self, kind: str, name: str, namespace: str, api_group: str = None):
        self._role_binding.subjects.append(client.V1Subject(
            api_group=api_group, kind=kind, name=name, namespace=namespace))


class Role(_Role):
    def __init__(self, name: str):
        super().__init__(name, 'Role')


class RoleBinding(_RoleBinding):
    def __init__(self, name: str):
        super().__init__(name, 'RoleBinding')


class ClusterRole(_Role):
    def __init__(self, name: str):
        super().__init__(name, 'ClusterRole')

    def add_aggregation_rule(self, rule: client.V1LabelSelector):
        if not self._role.aggregation_rule:
            self._role.aggregation_rule = client.V1AggregationRule(
                cluster_role_selectors=[]
            )

        self._role.aggregation_rule.cluster_role_selectors.append(rule)


class ClusterRoleBinding(_RoleBinding):
    def __init__(self, name: str):
        super().__init__(name, 'ClusterRoleBinding')
