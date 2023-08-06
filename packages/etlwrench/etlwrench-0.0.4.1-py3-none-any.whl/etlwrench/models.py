from pydantic import BaseModel, Field
from datetime import datetime

class Contact(BaseModel):
    name: str = Field(alias="name")
    email: str = Field(alias="email")

class Module(BaseModel):
    identifier: str = Field(alias="identifier")
    version: float = Field(alias="version")
    contact: Contact = Field(alias="contact")
    mounted: bool = Field(alias="mounted")
    marked_for_deletion: bool = Field(alias="mark-for-deletion")

class Cluster(BaseModel):
    identifier: str = Field(alias="id")
    mounted: bool = Field(alias="mounted")

class ProvisionResponse(BaseModel):
    id: int = Field(alias="id")
    cluster: str = Field(alias="cluster")

class Config(BaseModel):
    identifier: str = Field(alias="identifier")
    on_load: str = Field(alias="on-load")
    on_crash: str = Field(alias="on-crash")
    start_with_n_t_channels: int = Field(alias="start-with-n-t-channels")
    start_with_n_l_channels: int = Field(alias="start-with-n-l-channels")
    et_channel_threshold: int = Field(alias="et-channel-threshold")
    et_channel_growth_factor: int = Field(alias="et-channel-growth-factor")
    tl_channel_threshold: int = Field(alias="tl-channel-threshold")
    tl_channel_growth_factor: int = Field(alias="tl-channel-growth-factor")

class ThreadStatistics(BaseModel):
    num_provisioned_extract_routines: int = Field(alias="num-provisioned-extract-routines")
    num_provisioned_transform_routines: int = Field(alias="num-provisioned-transform-routes")
    num_provisioned_load_routines: int = Field(alias="num-provisioned-load-routines")

class ChannelStatistics(BaseModel):
    num_et_threshold_breaches: int = Field(alias="num-et-threshold-breaches")
    num_tl_threshold_breaches: int = Field(alias="num-tl-threshold-breaches")

class DataStatistics(BaseModel):
    total_processed: int = Field(alias="total-processed")
    total_over_et: int = Field(alias="total-over-et")
    total_over_tl: int = Field(alias="total-over-tl")
    total_dropped: int = Field(alias="total-dropped")

class ChannelTimingStatistics(BaseModel):
    min_time_before_pop_ns: int = Field(alias="min-time-before-pop-ns")
    max_time_before_pop_ns: int = Field(alias="max-time-before-pop-ns")
    average_time_ns: int = Field(alias="average-time-ns")
    average_time_ns: int = Field(alias="median-time-ns")

class TimingStatistics(BaseModel):
    et_channel: ChannelTimingStatistics = Field(alias="et-channel")
    tl_channel: ChannelTimingStatistics = Field(alias="tl-channel")
    min_total_time_ns: int = Field(alias="min-total-time-ns")
    max_total_time_ns: int = Field(alias="max-total-time-ns")
    average_time_ns: int = Field(alias="avg-total-time-ns")
    median_time_ns: int = Field(alias="med-total-time-ns")
    
class Statistics(BaseModel):
    threads: ThreadStatistics = Field(alias="threads")
    channels: ChannelStatistics = Field(alias="channels")
    data: DataStatistics = Field(alias="data")
    timing: TimingStatistics = Field(alias="timing")

class ShortConfig(BaseModel):
    threshold: int = Field(alias="Threshold")
    growth_factor: int = Field(alias="GrowthFactor")

class ChannelDataTimestamp(BaseModel):
    data_in: datetime = Field(alias="In")
    data_out: datetime = Field(alias="Out")

class Channel(BaseModel):
    name: str = Field(alias="Name")
    state: int = Field(alias="State")
    size: int = Field(alias="Size")
    config: ShortConfig = Field(alias="Config")
    total_processed: int = Field(alias="TotalProcessed")
    timestamps: dict[str, ChannelDataTimestamp] = Field(alias="Timestamps")
    last_push: datetime = Field(alias="LastPush")
    channel_finished: bool = Field(alias="ChannelFinished")

class Supervisor(BaseModel):
    id: int = Field(alias="id")
    config: Config = Field(alias="config")
    statistics: Statistics = Field(alias="stats")
    status: str = Field(alias="status")
    on_crash: str = Field(alias="on-crash")
    start_time: datetime = Field(alias="start-time")
    et_channel: Channel = Field(alias="ETChannel")
    tl_channel: Channel = Field(alias="TLChannel")