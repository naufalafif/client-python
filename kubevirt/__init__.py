# coding: utf-8

"""
    KubeVirt API

    This is KubeVirt API an add-on for Kubernetes.

    OpenAPI spec version: 1.0.0
    Contact: kubevirt-dev@googlegroups.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into sdk package
from .models.k8s_io_api_core_v1_affinity import K8sIoApiCoreV1Affinity
from .models.k8s_io_api_core_v1_downward_api_volume_file import K8sIoApiCoreV1DownwardAPIVolumeFile
from .models.k8s_io_api_core_v1_exec_action import K8sIoApiCoreV1ExecAction
from .models.k8s_io_api_core_v1_http_get_action import K8sIoApiCoreV1HTTPGetAction
from .models.k8s_io_api_core_v1_http_header import K8sIoApiCoreV1HTTPHeader
from .models.k8s_io_api_core_v1_local_object_reference import K8sIoApiCoreV1LocalObjectReference
from .models.k8s_io_api_core_v1_node_affinity import K8sIoApiCoreV1NodeAffinity
from .models.k8s_io_api_core_v1_node_selector import K8sIoApiCoreV1NodeSelector
from .models.k8s_io_api_core_v1_node_selector_requirement import K8sIoApiCoreV1NodeSelectorRequirement
from .models.k8s_io_api_core_v1_node_selector_term import K8sIoApiCoreV1NodeSelectorTerm
from .models.k8s_io_api_core_v1_object_field_selector import K8sIoApiCoreV1ObjectFieldSelector
from .models.k8s_io_api_core_v1_persistent_volume_claim_spec import K8sIoApiCoreV1PersistentVolumeClaimSpec
from .models.k8s_io_api_core_v1_persistent_volume_claim_volume_source import K8sIoApiCoreV1PersistentVolumeClaimVolumeSource
from .models.k8s_io_api_core_v1_pod_affinity import K8sIoApiCoreV1PodAffinity
from .models.k8s_io_api_core_v1_pod_affinity_term import K8sIoApiCoreV1PodAffinityTerm
from .models.k8s_io_api_core_v1_pod_anti_affinity import K8sIoApiCoreV1PodAntiAffinity
from .models.k8s_io_api_core_v1_pod_dns_config import K8sIoApiCoreV1PodDNSConfig
from .models.k8s_io_api_core_v1_pod_dns_config_option import K8sIoApiCoreV1PodDNSConfigOption
from .models.k8s_io_api_core_v1_preferred_scheduling_term import K8sIoApiCoreV1PreferredSchedulingTerm
from .models.k8s_io_api_core_v1_resource_field_selector import K8sIoApiCoreV1ResourceFieldSelector
from .models.k8s_io_api_core_v1_resource_requirements import K8sIoApiCoreV1ResourceRequirements
from .models.k8s_io_api_core_v1_tcp_socket_action import K8sIoApiCoreV1TCPSocketAction
from .models.k8s_io_api_core_v1_toleration import K8sIoApiCoreV1Toleration
from .models.k8s_io_api_core_v1_typed_local_object_reference import K8sIoApiCoreV1TypedLocalObjectReference
from .models.k8s_io_api_core_v1_weighted_pod_affinity_term import K8sIoApiCoreV1WeightedPodAffinityTerm
from .models.k8s_io_apimachinery_pkg_api_resource_quantity import K8sIoApimachineryPkgApiResourceQuantity
from .models.k8s_io_apimachinery_pkg_apis_meta_v1_api_group import K8sIoApimachineryPkgApisMetaV1APIGroup
from .models.k8s_io_apimachinery_pkg_apis_meta_v1_api_group_list import K8sIoApimachineryPkgApisMetaV1APIGroupList
from .models.k8s_io_apimachinery_pkg_apis_meta_v1_api_resource import K8sIoApimachineryPkgApisMetaV1APIResource
from .models.k8s_io_apimachinery_pkg_apis_meta_v1_api_resource_list import K8sIoApimachineryPkgApisMetaV1APIResourceList
from .models.k8s_io_apimachinery_pkg_apis_meta_v1_delete_options import K8sIoApimachineryPkgApisMetaV1DeleteOptions
from .models.k8s_io_apimachinery_pkg_apis_meta_v1_duration import K8sIoApimachineryPkgApisMetaV1Duration
from .models.k8s_io_apimachinery_pkg_apis_meta_v1_fields_v1 import K8sIoApimachineryPkgApisMetaV1FieldsV1
from .models.k8s_io_apimachinery_pkg_apis_meta_v1_group_version_for_discovery import K8sIoApimachineryPkgApisMetaV1GroupVersionForDiscovery
from .models.k8s_io_apimachinery_pkg_apis_meta_v1_label_selector import K8sIoApimachineryPkgApisMetaV1LabelSelector
from .models.k8s_io_apimachinery_pkg_apis_meta_v1_label_selector_requirement import K8sIoApimachineryPkgApisMetaV1LabelSelectorRequirement
from .models.k8s_io_apimachinery_pkg_apis_meta_v1_list_meta import K8sIoApimachineryPkgApisMetaV1ListMeta
from .models.k8s_io_apimachinery_pkg_apis_meta_v1_managed_fields_entry import K8sIoApimachineryPkgApisMetaV1ManagedFieldsEntry
from .models.k8s_io_apimachinery_pkg_apis_meta_v1_object_meta import K8sIoApimachineryPkgApisMetaV1ObjectMeta
from .models.k8s_io_apimachinery_pkg_apis_meta_v1_owner_reference import K8sIoApimachineryPkgApisMetaV1OwnerReference
from .models.k8s_io_apimachinery_pkg_apis_meta_v1_patch import K8sIoApimachineryPkgApisMetaV1Patch
from .models.k8s_io_apimachinery_pkg_apis_meta_v1_preconditions import K8sIoApimachineryPkgApisMetaV1Preconditions
from .models.k8s_io_apimachinery_pkg_apis_meta_v1_root_paths import K8sIoApimachineryPkgApisMetaV1RootPaths
from .models.k8s_io_apimachinery_pkg_apis_meta_v1_server_address_by_client_cidr import K8sIoApimachineryPkgApisMetaV1ServerAddressByClientCIDR
from .models.k8s_io_apimachinery_pkg_apis_meta_v1_status import K8sIoApimachineryPkgApisMetaV1Status
from .models.k8s_io_apimachinery_pkg_apis_meta_v1_status_cause import K8sIoApimachineryPkgApisMetaV1StatusCause
from .models.k8s_io_apimachinery_pkg_apis_meta_v1_status_details import K8sIoApimachineryPkgApisMetaV1StatusDetails
from .models.k8s_io_apimachinery_pkg_apis_meta_v1_time import K8sIoApimachineryPkgApisMetaV1Time
from .models.k8s_io_apimachinery_pkg_apis_meta_v1_watch_event import K8sIoApimachineryPkgApisMetaV1WatchEvent
from .models.k8s_io_apimachinery_pkg_runtime_raw_extension import K8sIoApimachineryPkgRuntimeRawExtension
from .models.k8s_io_apimachinery_pkg_util_intstr_int_or_string import K8sIoApimachineryPkgUtilIntstrIntOrString
from .models.v1_access_credential import V1AccessCredential
from .models.v1_access_credential_secret_source import V1AccessCredentialSecretSource
from .models.v1_add_volume_options import V1AddVolumeOptions
from .models.v1_bios import V1BIOS
from .models.v1_block_size import V1BlockSize
from .models.v1_bootloader import V1Bootloader
from .models.v1_cd_rom_target import V1CDRomTarget
from .models.v1_cpu import V1CPU
from .models.v1_cpu_feature import V1CPUFeature
from .models.v1_cert_config import V1CertConfig
from .models.v1_chassis import V1Chassis
from .models.v1_client_passthrough_devices import V1ClientPassthroughDevices
from .models.v1_clock import V1Clock
from .models.v1_clock_offset_utc import V1ClockOffsetUTC
from .models.v1_cloud_init_config_drive_source import V1CloudInitConfigDriveSource
from .models.v1_cloud_init_no_cloud_source import V1CloudInitNoCloudSource
from .models.v1_component_config import V1ComponentConfig
from .models.v1_config_drive_ssh_public_key_access_credential_propagation import V1ConfigDriveSSHPublicKeyAccessCredentialPropagation
from .models.v1_config_map_volume_source import V1ConfigMapVolumeSource
from .models.v1_container_disk_source import V1ContainerDiskSource
from .models.v1_custom_block_size import V1CustomBlockSize
from .models.v1_customize_components import V1CustomizeComponents
from .models.v1_customize_components_patch import V1CustomizeComponentsPatch
from .models.v1_dhcp_options import V1DHCPOptions
from .models.v1_dhcp_private_options import V1DHCPPrivateOptions
from .models.v1_data_volume_source import V1DataVolumeSource
from .models.v1_data_volume_template_dummy_status import V1DataVolumeTemplateDummyStatus
from .models.v1_data_volume_template_spec import V1DataVolumeTemplateSpec
from .models.v1_developer_configuration import V1DeveloperConfiguration
from .models.v1_devices import V1Devices
from .models.v1_disk import V1Disk
from .models.v1_disk_target import V1DiskTarget
from .models.v1_disk_verification import V1DiskVerification
from .models.v1_domain_spec import V1DomainSpec
from .models.v1_downward_api_volume_source import V1DownwardAPIVolumeSource
from .models.v1_downward_metrics_volume_source import V1DownwardMetricsVolumeSource
from .models.v1_efi import V1EFI
from .models.v1_empty_disk_source import V1EmptyDiskSource
from .models.v1_ephemeral_volume_source import V1EphemeralVolumeSource
from .models.v1_feature_apic import V1FeatureAPIC
from .models.v1_feature_hyperv import V1FeatureHyperv
from .models.v1_feature_kvm import V1FeatureKVM
from .models.v1_feature_spinlocks import V1FeatureSpinlocks
from .models.v1_feature_state import V1FeatureState
from .models.v1_feature_vendor_id import V1FeatureVendorID
from .models.v1_features import V1Features
from .models.v1_filesystem import V1Filesystem
from .models.v1_filesystem_virtiofs import V1FilesystemVirtiofs
from .models.v1_firmware import V1Firmware
from .models.v1_flags import V1Flags
from .models.v1_flavor_matcher import V1FlavorMatcher
from .models.v1_floppy_target import V1FloppyTarget
from .models.v1_freeze_unfreeze_timeout import V1FreezeUnfreezeTimeout
from .models.v1_gpu import V1GPU
from .models.v1_generation_status import V1GenerationStatus
from .models.v1_guest_agent_command_info import V1GuestAgentCommandInfo
from .models.v1_guest_agent_ping import V1GuestAgentPing
from .models.v1_hpet_timer import V1HPETTimer
from .models.v1_host_device import V1HostDevice
from .models.v1_host_disk import V1HostDisk
from .models.v1_hotplug_volume_source import V1HotplugVolumeSource
from .models.v1_hotplug_volume_status import V1HotplugVolumeStatus
from .models.v1_hugepages import V1Hugepages
from .models.v1_hyperv_timer import V1HypervTimer
from .models.v1_i6300_esb_watchdog import V1I6300ESBWatchdog
from .models.v1_input import V1Input
from .models.v1_interface import V1Interface
from .models.v1_interface_bridge import V1InterfaceBridge
from .models.v1_interface_macvtap import V1InterfaceMacvtap
from .models.v1_interface_masquerade import V1InterfaceMasquerade
from .models.v1_interface_sriov import V1InterfaceSRIOV
from .models.v1_interface_slirp import V1InterfaceSlirp
from .models.v1_kvm_timer import V1KVMTimer
from .models.v1_kernel_boot import V1KernelBoot
from .models.v1_kernel_boot_container import V1KernelBootContainer
from .models.v1_kube_virt import V1KubeVirt
from .models.v1_kube_virt_certificate_rotate_strategy import V1KubeVirtCertificateRotateStrategy
from .models.v1_kube_virt_condition import V1KubeVirtCondition
from .models.v1_kube_virt_configuration import V1KubeVirtConfiguration
from .models.v1_kube_virt_list import V1KubeVirtList
from .models.v1_kube_virt_self_sign_configuration import V1KubeVirtSelfSignConfiguration
from .models.v1_kube_virt_spec import V1KubeVirtSpec
from .models.v1_kube_virt_status import V1KubeVirtStatus
from .models.v1_kube_virt_workload_update_strategy import V1KubeVirtWorkloadUpdateStrategy
from .models.v1_log_verbosity import V1LogVerbosity
from .models.v1_lun_target import V1LunTarget
from .models.v1_machine import V1Machine
from .models.v1_mediated_devices_configuration import V1MediatedDevicesConfiguration
from .models.v1_mediated_host_device import V1MediatedHostDevice
from .models.v1_memory import V1Memory
from .models.v1_migrate_options import V1MigrateOptions
from .models.v1_migration_configuration import V1MigrationConfiguration
from .models.v1_multus_network import V1MultusNetwork
from .models.v1_numa import V1NUMA
from .models.v1_numa_guest_mapping_passthrough import V1NUMAGuestMappingPassthrough
from .models.v1_network import V1Network
from .models.v1_network_configuration import V1NetworkConfiguration
from .models.v1_node_placement import V1NodePlacement
from .models.v1_pit_timer import V1PITTimer
from .models.v1_pause_options import V1PauseOptions
from .models.v1_pci_host_device import V1PciHostDevice
from .models.v1_permitted_host_devices import V1PermittedHostDevices
from .models.v1_persistent_volume_claim_info import V1PersistentVolumeClaimInfo
from .models.v1_persistent_volume_claim_volume_source import V1PersistentVolumeClaimVolumeSource
from .models.v1_pod_network import V1PodNetwork
from .models.v1_port import V1Port
from .models.v1_probe import V1Probe
from .models.v1_qemu_guest_agent_ssh_public_key_access_credential_propagation import V1QemuGuestAgentSSHPublicKeyAccessCredentialPropagation
from .models.v1_qemu_guest_agent_user_password_access_credential_propagation import V1QemuGuestAgentUserPasswordAccessCredentialPropagation
from .models.v1_rest_client_configuration import V1RESTClientConfiguration
from .models.v1_rtc_timer import V1RTCTimer
from .models.v1_rate_limiter import V1RateLimiter
from .models.v1_realtime import V1Realtime
from .models.v1_reloadable_component_configuration import V1ReloadableComponentConfiguration
from .models.v1_remove_volume_options import V1RemoveVolumeOptions
from .models.v1_resource_requirements import V1ResourceRequirements
from .models.v1_restart_options import V1RestartOptions
from .models.v1_rng import V1Rng
from .models.v1_sm_bios_configuration import V1SMBiosConfiguration
from .models.v1_ssh_public_key_access_credential import V1SSHPublicKeyAccessCredential
from .models.v1_ssh_public_key_access_credential_propagation_method import V1SSHPublicKeyAccessCredentialPropagationMethod
from .models.v1_ssh_public_key_access_credential_source import V1SSHPublicKeyAccessCredentialSource
from .models.v1_secret_volume_source import V1SecretVolumeSource
from .models.v1_service_account_volume_source import V1ServiceAccountVolumeSource
from .models.v1_sound_device import V1SoundDevice
from .models.v1_start_options import V1StartOptions
from .models.v1_stop_options import V1StopOptions
from .models.v1_sy_nic_timer import V1SyNICTimer
from .models.v1_sysprep_source import V1SysprepSource
from .models.v1_timer import V1Timer
from .models.v1_token_bucket_rate_limiter import V1TokenBucketRateLimiter
from .models.v1_topology_hints import V1TopologyHints
from .models.v1_unpause_options import V1UnpauseOptions
from .models.v1_user_password_access_credential import V1UserPasswordAccessCredential
from .models.v1_user_password_access_credential_propagation_method import V1UserPasswordAccessCredentialPropagationMethod
from .models.v1_user_password_access_credential_source import V1UserPasswordAccessCredentialSource
from .models.v1_vgpu_display_options import V1VGPUDisplayOptions
from .models.v1_vgpu_options import V1VGPUOptions
from .models.v1_virtual_machine import V1VirtualMachine
from .models.v1_virtual_machine_condition import V1VirtualMachineCondition
from .models.v1_virtual_machine_instance import V1VirtualMachineInstance
from .models.v1_virtual_machine_instance_condition import V1VirtualMachineInstanceCondition
from .models.v1_virtual_machine_instance_file_system import V1VirtualMachineInstanceFileSystem
from .models.v1_virtual_machine_instance_file_system_info import V1VirtualMachineInstanceFileSystemInfo
from .models.v1_virtual_machine_instance_file_system_list import V1VirtualMachineInstanceFileSystemList
from .models.v1_virtual_machine_instance_guest_agent_info import V1VirtualMachineInstanceGuestAgentInfo
from .models.v1_virtual_machine_instance_guest_os_info import V1VirtualMachineInstanceGuestOSInfo
from .models.v1_virtual_machine_instance_guest_os_user import V1VirtualMachineInstanceGuestOSUser
from .models.v1_virtual_machine_instance_guest_os_user_list import V1VirtualMachineInstanceGuestOSUserList
from .models.v1_virtual_machine_instance_list import V1VirtualMachineInstanceList
from .models.v1_virtual_machine_instance_migration import V1VirtualMachineInstanceMigration
from .models.v1_virtual_machine_instance_migration_condition import V1VirtualMachineInstanceMigrationCondition
from .models.v1_virtual_machine_instance_migration_list import V1VirtualMachineInstanceMigrationList
from .models.v1_virtual_machine_instance_migration_spec import V1VirtualMachineInstanceMigrationSpec
from .models.v1_virtual_machine_instance_migration_state import V1VirtualMachineInstanceMigrationState
from .models.v1_virtual_machine_instance_migration_status import V1VirtualMachineInstanceMigrationStatus
from .models.v1_virtual_machine_instance_network_interface import V1VirtualMachineInstanceNetworkInterface
from .models.v1_virtual_machine_instance_phase_transition_timestamp import V1VirtualMachineInstancePhaseTransitionTimestamp
from .models.v1_virtual_machine_instance_preset import V1VirtualMachineInstancePreset
from .models.v1_virtual_machine_instance_preset_list import V1VirtualMachineInstancePresetList
from .models.v1_virtual_machine_instance_preset_spec import V1VirtualMachineInstancePresetSpec
from .models.v1_virtual_machine_instance_replica_set import V1VirtualMachineInstanceReplicaSet
from .models.v1_virtual_machine_instance_replica_set_condition import V1VirtualMachineInstanceReplicaSetCondition
from .models.v1_virtual_machine_instance_replica_set_list import V1VirtualMachineInstanceReplicaSetList
from .models.v1_virtual_machine_instance_replica_set_spec import V1VirtualMachineInstanceReplicaSetSpec
from .models.v1_virtual_machine_instance_replica_set_status import V1VirtualMachineInstanceReplicaSetStatus
from .models.v1_virtual_machine_instance_spec import V1VirtualMachineInstanceSpec
from .models.v1_virtual_machine_instance_status import V1VirtualMachineInstanceStatus
from .models.v1_virtual_machine_instance_template_spec import V1VirtualMachineInstanceTemplateSpec
from .models.v1_virtual_machine_list import V1VirtualMachineList
from .models.v1_virtual_machine_spec import V1VirtualMachineSpec
from .models.v1_virtual_machine_start_failure import V1VirtualMachineStartFailure
from .models.v1_virtual_machine_state_change_request import V1VirtualMachineStateChangeRequest
from .models.v1_virtual_machine_status import V1VirtualMachineStatus
from .models.v1_virtual_machine_volume_request import V1VirtualMachineVolumeRequest
from .models.v1_volume import V1Volume
from .models.v1_volume_snapshot_status import V1VolumeSnapshotStatus
from .models.v1_volume_status import V1VolumeStatus
from .models.v1_watchdog import V1Watchdog
from .models.v1alpha1_condition import V1alpha1Condition
from .models.v1alpha1_error import V1alpha1Error
from .models.v1alpha1_migration_policy import V1alpha1MigrationPolicy
from .models.v1alpha1_migration_policy_list import V1alpha1MigrationPolicyList
from .models.v1alpha1_migration_policy_spec import V1alpha1MigrationPolicySpec
from .models.v1alpha1_migration_policy_status import V1alpha1MigrationPolicyStatus
from .models.v1alpha1_persistent_volume_claim import V1alpha1PersistentVolumeClaim
from .models.v1alpha1_selectors import V1alpha1Selectors
from .models.v1alpha1_source_spec import V1alpha1SourceSpec
from .models.v1alpha1_virtual_machine_cluster_flavor import V1alpha1VirtualMachineClusterFlavor
from .models.v1alpha1_virtual_machine_cluster_flavor_list import V1alpha1VirtualMachineClusterFlavorList
from .models.v1alpha1_virtual_machine_flavor import V1alpha1VirtualMachineFlavor
from .models.v1alpha1_virtual_machine_flavor_list import V1alpha1VirtualMachineFlavorList
from .models.v1alpha1_virtual_machine_flavor_profile import V1alpha1VirtualMachineFlavorProfile
from .models.v1alpha1_virtual_machine_pool import V1alpha1VirtualMachinePool
from .models.v1alpha1_virtual_machine_pool_condition import V1alpha1VirtualMachinePoolCondition
from .models.v1alpha1_virtual_machine_pool_list import V1alpha1VirtualMachinePoolList
from .models.v1alpha1_virtual_machine_pool_spec import V1alpha1VirtualMachinePoolSpec
from .models.v1alpha1_virtual_machine_pool_status import V1alpha1VirtualMachinePoolStatus
from .models.v1alpha1_virtual_machine_restore import V1alpha1VirtualMachineRestore
from .models.v1alpha1_virtual_machine_restore_list import V1alpha1VirtualMachineRestoreList
from .models.v1alpha1_virtual_machine_restore_spec import V1alpha1VirtualMachineRestoreSpec
from .models.v1alpha1_virtual_machine_restore_status import V1alpha1VirtualMachineRestoreStatus
from .models.v1alpha1_virtual_machine_snapshot import V1alpha1VirtualMachineSnapshot
from .models.v1alpha1_virtual_machine_snapshot_content import V1alpha1VirtualMachineSnapshotContent
from .models.v1alpha1_virtual_machine_snapshot_content_list import V1alpha1VirtualMachineSnapshotContentList
from .models.v1alpha1_virtual_machine_snapshot_content_spec import V1alpha1VirtualMachineSnapshotContentSpec
from .models.v1alpha1_virtual_machine_snapshot_content_status import V1alpha1VirtualMachineSnapshotContentStatus
from .models.v1alpha1_virtual_machine_snapshot_list import V1alpha1VirtualMachineSnapshotList
from .models.v1alpha1_virtual_machine_snapshot_spec import V1alpha1VirtualMachineSnapshotSpec
from .models.v1alpha1_virtual_machine_snapshot_status import V1alpha1VirtualMachineSnapshotStatus
from .models.v1alpha1_virtual_machine_template_spec import V1alpha1VirtualMachineTemplateSpec
from .models.v1alpha1_volume_backup import V1alpha1VolumeBackup
from .models.v1alpha1_volume_restore import V1alpha1VolumeRestore
from .models.v1alpha1_volume_snapshot_status import V1alpha1VolumeSnapshotStatus
from .models.v1beta1_data_volume_blank_image import V1beta1DataVolumeBlankImage
from .models.v1beta1_data_volume_checkpoint import V1beta1DataVolumeCheckpoint
from .models.v1beta1_data_volume_source import V1beta1DataVolumeSource
from .models.v1beta1_data_volume_source_http import V1beta1DataVolumeSourceHTTP
from .models.v1beta1_data_volume_source_image_io import V1beta1DataVolumeSourceImageIO
from .models.v1beta1_data_volume_source_pvc import V1beta1DataVolumeSourcePVC
from .models.v1beta1_data_volume_source_ref import V1beta1DataVolumeSourceRef
from .models.v1beta1_data_volume_source_registry import V1beta1DataVolumeSourceRegistry
from .models.v1beta1_data_volume_source_s3 import V1beta1DataVolumeSourceS3
from .models.v1beta1_data_volume_source_upload import V1beta1DataVolumeSourceUpload
from .models.v1beta1_data_volume_source_vddk import V1beta1DataVolumeSourceVDDK
from .models.v1beta1_data_volume_spec import V1beta1DataVolumeSpec
from .models.v1beta1_storage_spec import V1beta1StorageSpec

# import apis into sdk package
from .apis.default_api import DefaultApi

# import ApiClient
from .api_client import ApiClient

from .configuration import Configuration

configuration = Configuration()
from .models.v1_interface_bridge import V1InterfaceBridge
from .models.v1_interface_slirp import V1InterfaceSlirp
