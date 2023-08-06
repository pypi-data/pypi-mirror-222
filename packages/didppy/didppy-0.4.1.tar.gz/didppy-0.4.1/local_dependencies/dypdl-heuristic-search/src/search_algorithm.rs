//! A module for search algorithms.

mod acps;
mod apps;
mod beam_search;
mod best_first_search;
mod breadth_first_search;
mod cabs;
mod cbfs;
pub mod data_structure;
mod dbdfs;
mod dfbb;
mod forward_recursion;
mod rollout;
mod search;
pub mod util;

pub use acps::{Acps, ProgressiveSearchParameters};
pub use apps::Apps;
pub use beam_search::{beam_search, BeamSearchParameters};
pub use best_first_search::BestFirstSearch;
pub use breadth_first_search::{BreadthFirstSearch, BrfsParameters};
pub use cabs::{Cabs, CabsParameters};
pub use cbfs::Cbfs;
pub use data_structure::{
    BfsNode, CostNode, CustomFNode, FNode, StateInRegistry, StateRegistry, SuccessorGenerator,
    TransitionWithCustomCost, TransitionWithId, WeightedFNode,
};
pub use dbdfs::{Dbdfs, DbdfsParameters};
pub use dfbb::Dfbb;
pub use forward_recursion::ForwardRecursion;
pub use rollout::{get_solution_cost_and_suffix, get_trace, rollout, RolloutResult};
pub use search::{Parameters, Search, SearchInput, Solution};
